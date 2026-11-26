from uuid import UUID

from rest_framework import serializers, status
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from core.member.use_case.calculate_member_rank import (
    CalculateMemberRankUseCaseInput,
    MemberNotFoundError,
)
from di.container import create_calculate_member_rank_use_case


# uidのバリデーションを行うためのシリアライザを定義
class CalculateMemberRankRequestSerializer(serializers.Serializer):
    uid = serializers.CharField(
        required=True,
        allow_blank=False,
    )

    def validate_uid(self, value: str) -> str:
        try:
            UUID(value)
        except ValueError:
            raise serializers.ValidationError("Invalid UUID format.")

        return value


class CalculateMemberRankView(APIView):
    def get(self, request, uid: str) -> Response:
        # パスパラメータのバリデーションチェック
        serializer = CalculateMemberRankRequestSerializer(data={"uid": uid})
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        # ユースケースの実行
        use_case = create_calculate_member_rank_use_case()

        try:
            result = use_case.execute(
                CalculateMemberRankUseCaseInput(
                    uid=validated_data["uid"],
                ),
            )
        except ValueError as exc:
            raise ValidationError({"uid": str(exc)}) from exc
        except MemberNotFoundError as exc:
            raise NotFound("Member not found.") from exc

        # レスポンス結果
        return Response(
            {"rank": result.rank},
            status=status.HTTP_200_OK,
        )
