from rest_framework.response import Response
from rest_framework.views import APIView

from di.container import create_hello_use_case


class HelloView(APIView):
    def get(self, request):
        # ユースケースの実行
        use_case = create_hello_use_case()
        result = use_case.execute()

        return Response(result)
