from rest_framework import status
from rest_framework.test import APIClient


class TestHelloIntegration:
    def test_get(self):
        # テストクライアント作成
        client = APIClient()

        # リクエスト実行
        response = client.get("/api/v1/hello/")

        # HTTPレスポンスの検証
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {"message": "Hello World !!"}
