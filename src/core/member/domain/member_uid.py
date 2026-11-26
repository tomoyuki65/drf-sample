import uuid


class MemberUid:
    def __init__(self, value: str) -> None:
        # UUIDが有効かをチェック
        try:
            parsed_uid = uuid.UUID(value)
        except (ValueError, TypeError, AttributeError) as exc:
            raise ValueError(f"Invalid MemberUid: {value}") from exc

        # 入力値の形式をチェック
        if str(parsed_uid) != value.lower():
            raise ValueError(f"Invalid MemberUid: {value}")

        self._value = str(parsed_uid)

    @property
    def value(self) -> str:
        return self._value
