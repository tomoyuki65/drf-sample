from dataclasses import dataclass
from decimal import Decimal

from core.member.domain.member_uid import MemberUid


@dataclass(frozen=True)
class Member:
    uid: MemberUid
    last_name: str
    first_name: str
    total_purchase_amount: Decimal

    # フルネームを返すプロパティを追加
    @property
    def full_name(self) -> str:
        return f"{self.last_name} {self.first_name}"
