import uuid

from django.db import models


class UserModel(models.Model):
    id = models.BigAutoField(primary_key=True)

    uid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    last_name = models.TextField()

    first_name = models.TextField()

    total_purchase_amount = models.IntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        db_table = "users"
        indexes = [
            models.Index(
                fields=["last_name"],
                name="users_last_name_idx",
            ),
        ]
