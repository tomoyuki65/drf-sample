FROM python:3.15.2-slim-trixie

# タイムゾーン設定
ENV TZ=Asia/Tokyo

# uvをインストール
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# uvの設定
ENV UV_LINK_MODE=copy
ENV UV_PROJECT_ENVIRONMENT=/app/.venv

WORKDIR /app

COPY . .

EXPOSE 8000
