import uuid

import pytest

from core.member.domain.member_uid import MemberUid


class TestMemberUid:
    def test_valid_uuid(self) -> None:
        """有効なUUIDを生成できること"""
        value = str(uuid.uuid4())

        member_uid = MemberUid(value)

        assert member_uid.value == value

    def test_valid_uppercase_uuid(self) -> None:
        """大文字が含まれるUUIDも許可されること"""
        value = str(uuid.uuid4()).upper()

        member_uid = MemberUid(value)

        assert member_uid.value == value.lower()

    @pytest.mark.parametrize(
        "value",
        [
            "invalid-uuid",
            "",
            "12345",
            "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            "550e8400-e29b-41d4-a716-446655440000-extra",
        ],
    )
    def test_invalid_uuid(self, value: str) -> None:
        """不正なUUIDを渡すとValueErrorが発生すること"""
        with pytest.raises(ValueError, match="Invalid MemberUid"):
            MemberUid(value)

    @pytest.mark.parametrize(
        "value",
        [
            None,
            123,
            [],
        ],
    )
    def test_invalid_type(self, value: object) -> None:
        """文字列以外を渡すとValueErrorが発生すること"""
        with pytest.raises(ValueError, match="Invalid MemberUid"):
            MemberUid(value)
