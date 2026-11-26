from decimal import Decimal

from core.member.domain.member import Member
from core.member.domain.member_repository import MemberRepository
from core.member.domain.member_uid import MemberUid
from infrastructure.database.models.user_model import UserModel


class PgMemberRepository(MemberRepository):
    def find_by_uid(
        self,
        uid: MemberUid,
    ) -> Member | None:
        # Django ORMを使用して、uidに一致するユーザーをデータベースから取得
        user_model = UserModel.objects.filter(
            uid=uid.value,
        ).first()

        # 取得したユーザーが存在しない場合はNoneを返す
        if user_model is None:
            return None

        return Member(
            uid=MemberUid(str(user_model.uid)),
            last_name=user_model.last_name,
            first_name=user_model.first_name,
            total_purchase_amount=Decimal(str(user_model.total_purchase_amount)),
        )
