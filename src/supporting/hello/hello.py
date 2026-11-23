import logging

logger = logging.getLogger(__name__)


class HelloUseCase:
    def execute(self) -> dict:
        # ログ出力
        logger.info("HelloUseCase executed !")

        # 戻り値を返す
        return {"message": "Hello World !!"}
