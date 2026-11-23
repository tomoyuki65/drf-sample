import logging
import uuid
from contextvars import ContextVar

from asgiref.sync import iscoroutinefunction
from django.utils.decorators import sync_and_async_middleware

request_id_var = ContextVar("request_id", default="-")


# リクエストIDを生成してContextVarにセットするミドルウェア
@sync_and_async_middleware
def request_id_middleware(get_response):

    # 非同期処理の判定
    if iscoroutinefunction(get_response):

        async def middleware(request):
            # request_idを生成してContextVarにセット
            request_id = str(uuid.uuid4())
            request.request_id = request_id
            token = request_id_var.set(request_id)

            try:
                # ログ出力
                logger = logging.getLogger(__name__)
                logger.info("Request started")

                # 処理実行
                response = await get_response(request)
                response["X-Request-ID"] = request_id

                return response
            finally:
                # 後処理
                request_id_var.reset(token)

    # 同期処理の場合
    else:

        def middleware(request):
            # request_idを生成してContextVarにセット
            request_id = str(uuid.uuid4())
            request.request_id = request_id
            token = request_id_var.set(request_id)

            try:
                # ログ出力
                logger = logging.getLogger(__name__)
                logger.info("Request started")

                # 処理実行
                response = get_response(request)
                response["X-Request-ID"] = request_id

                return response
            finally:
                # 後処理
                request_id_var.reset(token)

    return middleware


# request_idをログに出力するためのフィルター
class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request_id_var.get()
        return True
