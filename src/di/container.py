from core.member.domain.member_rank_service import (
    MemberRankService,
)
from core.member.infrastructure.persistence.pg.query.member_repository import (
    PgMemberRepository,
)
from core.member.use_case.calculate_member_rank import (
    CalculateMemberRankUseCase,
)
from supporting.hello.hello_use_case import HelloUseCase


def create_hello_use_case() -> HelloUseCase:
    return HelloUseCase()


def create_calculate_member_rank_use_case() -> CalculateMemberRankUseCase:
    member_repository = PgMemberRepository()
    member_rank_service = MemberRankService()

    return CalculateMemberRankUseCase(
        member_repository=member_repository,
        member_rank_service=member_rank_service,
    )
