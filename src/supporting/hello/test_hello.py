from supporting.hello.hello import HelloUseCase


class TestHelloUseCase:
    def test_execute(self):
        # ユースケース作成
        use_case = HelloUseCase()

        # テスト実行
        result = use_case.execute()

        # 検証
        assert result == {"message": "Hello World !!"}
