from enum import StrEnum

from core.member.domain.member import Member


class MemberRank(StrEnum):
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"
    PLATINUM = "platinum"


class MemberRankService:
    def calculate(self, member: Member) -> MemberRank:
        # 100万円以上でプラチナ
        if member.total_purchase_amount >= 1_000_000:
            return MemberRank.PLATINUM

        # 10万円以上でゴールド
        if member.total_purchase_amount >= 100_000:
            return MemberRank.GOLD

        # 1万円以上でシルバー
        if member.total_purchase_amount >= 10_000:
            return MemberRank.SILVER

        return MemberRank.BRONZE
