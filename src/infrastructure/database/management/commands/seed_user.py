from django.core.management.base import BaseCommand

from infrastructure.database.models import UserModel


class Command(BaseCommand):
    help = "Create a sample user"

    def handle(self, *args, **options):
        user = UserModel.objects.create(
            last_name="山田",
            first_name="太郎",
            total_purchase_amount=10000,
        )

        self.stdout.write(self.style.SUCCESS(f"Successfully created user: {user.uid}"))
