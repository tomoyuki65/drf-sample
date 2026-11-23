from unittest.mock import patch

from rest_framework import status
from rest_framework.test import APIClient


class TestHelloView:
    @patch("presentation.http.supporting.hello.hello_view.create_hello_use_case")
    def test_get(self, mock_create_use_case):
        # モック化
        mock_use_case = mock_create_use_case.return_value
        mock_use_case.execute.return_value = {"message": "Hello World !!"}

        # テストクライアント作成
        client = APIClient()

        # リクエスト実行
        response = client.get("/api/v1/hello/")

        # 検証
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {"message": "Hello World !!"}

        # ユースケースが呼び出されたことを検証
        mock_create_use_case.assert_called_once()
        mock_use_case.execute.assert_called_once()
