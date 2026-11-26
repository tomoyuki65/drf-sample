from dataclasses import FrozenInstanceError
from decimal import Decimal

import pytest

from core.member.domain.member import Member
from core.member.domain.member_uid import MemberUid


class TestMember:
    def test_create_member(self) -> None:
        """有効なMemberを生成できること"""
        uid = MemberUid("550e8400-e29b-41d4-a716-446655440000")
        member = Member(
            uid=uid,
            last_name="山田",
            first_name="太郎",
            total_purchase_amount=Decimal("10000.00"),
        )

        assert member.uid == uid
        assert member.last_name == "山田"
        assert member.first_name == "太郎"
        assert member.total_purchase_amount == Decimal("10000.00")

    def test_full_name(self) -> None:
        """フルネームを取得できること"""
        member = Member(
            uid=MemberUid("550e8400-e29b-41d4-a716-446655440000"),
            last_name="山田",
            first_name="太郎",
            total_purchase_amount=Decimal("10000.00"),
        )

        assert member.full_name == "山田 太郎"

    def test_cannot_modify_uid(self) -> None:
        """uidを変更できないこと"""
        member = Member(
            uid=MemberUid("550e8400-e29b-41d4-a716-446655440000"),
            last_name="山田",
            first_name="太郎",
            total_purchase_amount=Decimal("10000.00"),
        )

        with pytest.raises(FrozenInstanceError):
            member.uid = MemberUid("550e8400-e29b-41d4-a716-446655440001")

    def test_cannot_modify_last_name(self) -> None:
        """last_nameを変更できないこと"""
        member = Member(
            uid=MemberUid("550e8400-e29b-41d4-a716-446655440000"),
            last_name="山田",
            first_name="太郎",
            total_purchase_amount=Decimal("10000.00"),
        )

        with pytest.raises(FrozenInstanceError):
            member.last_name = "佐藤"

    def test_cannot_modify_first_name(self) -> None:
        """first_nameを変更できないこと"""
        member = Member(
            uid=MemberUid("550e8400-e29b-41d4-a716-446655440000"),
            last_name="山田",
            first_name="太郎",
            total_purchase_amount=Decimal("10000.00"),
        )

        with pytest.raises(FrozenInstanceError):
            member.first_name = "花子"

    def test_cannot_modify_total_purchase_amount(self) -> None:
        """total_purchase_amountを変更できないこと"""
        member = Member(
            uid=MemberUid("550e8400-e29b-41d4-a716-446655440000"),
            last_name="山田",
            first_name="太郎",
            total_purchase_amount=Decimal("10000.00"),
        )

        with pytest.raises(FrozenInstanceError):
            member.total_purchase_amount = Decimal("20000.00")
