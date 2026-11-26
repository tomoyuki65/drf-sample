from decimal import Decimal
from unittest.mock import Mock

import pytest

from core.member.domain.member import Member
from core.member.domain.member_rank_service import (
    MemberRank,
    MemberRankService,
)
from core.member.domain.member_repository import MemberRepository
from core.member.domain.member_uid import MemberUid
from core.member.use_case.calculate_member_rank import (
    CalculateMemberRankUseCase,
    CalculateMemberRankUseCaseInput,
    MemberNotFoundError,
)


class TestCalculateMemberRankUseCase:
    @pytest.fixture
    def member_repository(self) -> Mock:
        return Mock(spec=MemberRepository)

    @pytest.fixture
    def member_rank_service(self) -> Mock:
        return Mock(spec=MemberRankService)

    @pytest.fixture
    def use_case(
        self,
        member_repository: Mock,
        member_rank_service: Mock,
    ) -> CalculateMemberRankUseCase:
        return CalculateMemberRankUseCase(
            member_repository=member_repository,
            member_rank_service=member_rank_service,
        )

    @pytest.fixture
    def member(self) -> Member:
        return Member(
            uid=MemberUid("550e8400-e29b-41d4-a716-446655440000"),
            last_name="山田",
            first_name="太郎",
            total_purchase_amount=Decimal(100000),
        )

    def test_execute_success(
        self,
        use_case: CalculateMemberRankUseCase,
        member_repository: Mock,
        member_rank_service: Mock,
        member: Member,
    ) -> None:
        """会員が存在する場合、会員ランクを取得できること"""
        # モック設定
        member_repository.find_by_uid.return_value = member
        member_rank_service.calculate.return_value = MemberRank.GOLD

        # 入力データ作成
        input = CalculateMemberRankUseCaseInput(
            uid="550e8400-e29b-41d4-a716-446655440000",
        )

        # テスト実行
        result = use_case.execute(input)

        # 検証
        assert result.rank == "gold"
        member_repository.find_by_uid.assert_called_once()
        member_rank_service.calculate.assert_called_once_with(member)

    def test_execute_member_not_found(
        self,
        use_case: CalculateMemberRankUseCase,
        member_repository: Mock,
        member_rank_service: Mock,
    ) -> None:
        """会員が存在しない場合、MemberNotFoundErrorが発生すること"""
        # モック設定
        member_repository.find_by_uid.return_value = None

        # 入力データ作成
        input = CalculateMemberRankUseCaseInput(
            uid="550e8400-e29b-41d4-a716-446655440000",
        )

        # 実行・検証
        with pytest.raises(MemberNotFoundError, match="Member not found."):
            use_case.execute(input)

        member_repository.find_by_uid.assert_called_once()
        member_rank_service.calculate.assert_not_called()

    def test_execute_invalid_uid(
        self,
        use_case: CalculateMemberRankUseCase,
        member_repository: Mock,
        member_rank_service: Mock,
    ) -> None:
        """不正なUIDの場合、ValueErrorが発生すること"""
        # 入力データ作成
        input = CalculateMemberRankUseCaseInput(
            uid="invalid-uuid",
        )

        # 実行・検証
        with pytest.raises(ValueError, match="Invalid MemberUid"):
            use_case.execute(input)

        member_repository.find_by_uid.assert_not_called()
        member_rank_service.calculate.assert_not_called()
