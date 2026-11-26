from dataclasses import dataclass

from core.member.domain.member_rank_service import (
    MemberRankService,
)
from core.member.domain.member_repository import (
    MemberRepository,
)
from core.member.domain.member_uid import MemberUid


class MemberNotFoundError(Exception):
    """会員が存在しない場合のエラー。"""

    def __init__(self) -> None:
        super().__init__("Member not found.")


@dataclass(frozen=True)
class CalculateMemberRankUseCaseInput:
    uid: str


@dataclass(frozen=True)
class CalculateMemberRankUseCaseOutput:
    rank: str


class CalculateMemberRankUseCase:
    def __init__(
        self,
        member_repository: MemberRepository,
        member_rank_service: MemberRankService,
    ) -> None:
        self._member_repository = member_repository
        self._member_rank_service = member_rank_service

    def execute(
        self,
        input: CalculateMemberRankUseCaseInput,
    ) -> CalculateMemberRankUseCaseOutput:
        # UIDの生成・バリデーション
        uid = MemberUid(input.uid)

        # UIDから会員を取得
        member = self._member_repository.find_by_uid(uid)

        # 会員の存在チェック
        if member is None:
            raise MemberNotFoundError()

        # 会員ランクの計算
        rank = self._member_rank_service.calculate(member)

        return CalculateMemberRankUseCaseOutput(
            rank=rank.value,
        )
