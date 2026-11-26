import pytest
from rest_framework.test import APIClient

from infrastructure.database.models.user_model import UserModel


@pytest.mark.django_db
def test_calculate_member_rank_success():
    """登録済みのユーザーのランクを取得できること"""
    # テスト用ユーザーを登録
    uid = "550e8400-e29b-41d4-a716-446655440000"

    UserModel.objects.create(
        uid=uid,
        last_name="山田",
        first_name="太郎",
        total_purchase_amount=10000,
    )

    # テストクライアント作成
    client = APIClient()

    # テスト実行
    response = client.get(f"/api/v1/members/{uid}/rank")

    # 検証
    assert response.status_code == 200
    assert response.json() == {"rank": "silver"}
