from types import SimpleNamespace
from unittest.mock import patch

import pytest
from rest_framework.test import APIClient

from core.member.use_case.calculate_member_rank import (
    CalculateMemberRankUseCaseInput,
)


# モック化
@pytest.fixture
def use_case_mock():
    with patch(
        "presentation.http.core.member.member_view."
        "create_calculate_member_rank_use_case"
    ) as mock:
        yield mock


def test_calculate_member_rank_success(use_case_mock):
    """正常なUIDの場合に200を返すこと"""
    # モック設定
    use_case = use_case_mock.return_value
    use_case.execute.return_value = SimpleNamespace(rank="gold")

    # テストクライアント作成
    client = APIClient()

    # リクエストパラメータ設定
    uid = "550e8400-e29b-41d4-a716-446655440000"

    # テスト実行
    response = client.get(f"/api/v1/members/{uid}/rank")

    # 検証
    assert response.status_code == 200
    assert response.json() == {"rank": "gold"}

    use_case.execute.assert_called_once_with(CalculateMemberRankUseCaseInput(uid=uid))


def test_calculate_member_rank_blank_uid(use_case_mock):
    """UIDが空白の場合に400を返し、ユースケースを実行しないこと"""
    # テストクライアント作成
    client = APIClient()

    # リクエストパラメータ設定
    uid = "%20"

    # テスト実行
    response = client.get(f"/api/v1/members/{uid}/rank")

    # 検証
    assert response.status_code == 400
    use_case_mock.return_value.execute.assert_not_called()


def test_calculate_member_rank_invalid_uid(use_case_mock):
    """UUID形式でないUIDの場合に400を返し、ユースケースを実行しないこと"""
    # テストクライアント作成
    client = APIClient()

    # リクエストパラメータ設定
    uid = "invalid-uid"

    # テスト実行
    response = client.get(f"/api/v1/members/{uid}/rank")

    # 検証
    assert response.status_code == 400
    use_case_mock.return_value.execute.assert_not_called()
