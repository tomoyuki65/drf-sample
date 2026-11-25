# Django REST framework（DRF）のサンプル
  
Pythonのフレームワーク「Django」、「Django REST framework（DRF）」を利用し、
バックエンドAPIを開発するためのサンプルです。
  
<br/>
  
## 動作要件
  
- Python: 3.15.2
- Django: 6.1.3
- Django REST framework: 3.18.3
- pytest: 9.2.0
- pytest-django: 4.14.0
- ruff: 0.17.6
  
<br/>
  
## ディレクトリ構成
  
今回のディレクトリ構成はDDD（ドメイン駆動設計）を前提としていますが、 それをアプリ全体に適用するのは本質的ではないため、 ３つの業務領域（中核、補完的、一般的）に分類することを前提としています。  
  
以上の方針を踏まえ、今回のディレクトリ構成は以下のように設計しています。  
  
```
/drf-sample
 └─ /src
     |
     ├─ /config（Djangoの設定）
     |
     ├─ /core（中核の業務領域）
     |   |
     |   └─ /[domain_name]（ドメインモジュール）
     |       |
     |       ├─ /domain（ドメイン）
     |       |   |
     |       |   ├─ [entity_name].py（エンティティ）
     |       |   |
     |       |   ├─ [value_object_name].py（値オブジェクト）
     |       |   |
     |       |   ├─ [domain_service_name]_service.py（ドメインサービス）
     |       |   |
     |       |   ├─ [repository_name]_repository.py（リポジトリのインターフェース）
     |       |   |
     |       |   └─ [gateway_name]_gateway.py（外部サービス用のインターフェース）
     |       |
     |       |
     |       ├─ /usecase（ユースケース層）
     |       |
     |       └─ /infrastructure（ドメイン用のインフラストラクチャ層）
     |           |
     |           ├─ /persistence（パーシステンス層）
     |           |   |
     |           |   └─ /pg（PostgreSQL用）
     |           |       |
     |           |       ├─ /command（書き込み）
     |           |       |
     |           |       └─ /query（読み込み）
     |           |
     |           └─ /external（外部サービスの実装）
     |
     ├─ /supporting（補完的なの業務領域）
     |   |
     |   └── /[supporting_name]（サービス層）
     |        |
     |        └─ [supporting_name]_use_case.py（ユースケース）
     |
     ├─ /generic（一般的な業務領域）
     |
     ├─ /shared（横断関心）
     |
     ├─ /di（DIコンテナ層）
     |   |
     |   └─ container.py
     |
     ├─ /infrastructure（共通のインフラストラクチャ層）
     |   |
     |   └─ /database（DB設定）
     |
     ├─ /presentation（プレゼンテーション層）
     |   |
     |   └─ /http
     |       |
     |       ├─ /core
     |       |   |
     |       |   └─ /[domain_name]
     |       |       |
     |       |       └─ [domain_name]_view.py
     |       |
     |       ├─ /supporting
     |       |   |
     |       |   └─ /[supporting_name]
     |       |       |
     |       |       └─ [supporting_name]_view.py
     |       |
     |       └─ /generic
     |
     └─  /tests（結合テスト用）
```
  
<br/>
  
## ローカル開発環境構築
  
### 1. 環境変数ファイルのリネーム
  
```
cp ./.env.example ./.env
```
  
---
  
### 2. Dockerコンテナのビルド
  
```
docker compose build --no-cache
```
  
---
  
### 3. 依存関係のインストール
  
```
docker compose run --rm drf uv sync --locked
```
  
---
  
### 4. サーバー起動
  
```
docker compose up -d
```
  
---
  
### 5. DBマイグレーションの実行
    
```
docker compose exec drf uv run python src/manage.py migrate database
```
> ※ マイグレーション状態を確認する場合は、コマンド「docker compose run --rm drf uv run python src/manage.py showmigrations」を実行して下さい。
  
> ※ usersテーブルに初期データを登録して試す場合、「docker compose run --rm drf uv run python src/manage.py seed_user」を実行して下さい。
  
---
  
### 6. Dockerコンテナの停止・削除
  
```
docker compose down
```
> ※ ボリュームも合わせて削除したい場合は、オプション「-v」を付けて実行して下さい。（例：docker compose down -v）
  
<br/>
  
## コード修正後に使うコマンド
  
### 1. フォーマット修正
  
```
docker compose run --rm drf uv run ruff format .
docker compose run --rm drf uv run ruff check . --select I --fix
```
  
---
  
### 2. コード解析チェック
  
```
docker compose run --rm drf uv run ruff check .
```
  
---
  
### 3. テストコード実行
  
```
docker compose exec drf uv run pytest
```
  
---
  
### 4. マイグレーションファイル作成用コマンド
  
```
docker compose exec drf uv run python src/manage.py makemigrations database
```
> ※「src/infrastructure/database/models」配下にモデル用ファイルを作成、または対象のファイル修正後、コマンドを実行するとマイグレーションファイルが自動生成されます。
  
<br/>
  
## APIのエンドポイント
  
Base URL: http://localhost:8000  
  
- GET /api/v1/hello  
  「{ "message": "Hello World !!" }」を出力
