from decimal import Decimal

import pytest

from core.member.domain.member import Member
from core.member.domain.member_rank_service import (
    MemberRank,
    MemberRankService,
)
from core.member.domain.member_uid import MemberUid


class TestMemberRankService:
    @pytest.fixture
    def service(self) -> MemberRankService:
        return MemberRankService()

    @pytest.mark.parametrize(
        ("total_purchase_amount", "expected_rank"),
        [
            # BRONZE
            (Decimal(0), MemberRank.BRONZE),
            (Decimal(9999), MemberRank.BRONZE),
            # SILVER
            (Decimal(10000), MemberRank.SILVER),
            (Decimal(99999), MemberRank.SILVER),
            # GOLD
            (Decimal(100000), MemberRank.GOLD),
            (Decimal(999999), MemberRank.GOLD),
            # PLATINUM
            (Decimal(1000000), MemberRank.PLATINUM),
            (Decimal(1500000), MemberRank.PLATINUM),
        ],
    )
    def test_calculate(
        self,
        service: MemberRankService,
        total_purchase_amount: Decimal,
        expected_rank: MemberRank,
    ) -> None:
        """購入金額に応じた会員ランクを取得できること"""
        member = Member(
            uid=MemberUid("550e8400-e29b-41d4-a716-446655440000"),
            last_name="山田",
            first_name="太郎",
            total_purchase_amount=total_purchase_amount,
        )

        result = service.calculate(member)

        assert result == expected_rank
