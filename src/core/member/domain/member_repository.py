from abc import ABC, abstractmethod

from core.member.domain.member import Member
from core.member.domain.member_uid import MemberUid


class MemberRepository(ABC):
    @abstractmethod
    def find_by_uid(
        self,
        uid: MemberUid,
    ) -> Member | None:
        """会員IDから対象ユーザーを取得"""
        raise NotImplementedError
