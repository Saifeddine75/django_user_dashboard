from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'List users grouped by privilege level'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        self.stdout.write("🟢 Superusers:")
        for user in User.objects.filter(is_superuser=True):
            self.stdout.write(f"- {user.email} (username: {user.username})")

        self.stdout.write("\n🟡 Staff (not superuser):")
        for user in User.objects.filter(is_staff=True, is_superuser=False):
            self.stdout.write(f"- {user.email} (username: {user.username})")

        self.stdout.write("\n🔵 Regular users:")
        for user in User.objects.filter(is_staff=False, is_superuser=False):
            self.stdout.write(f"- {user.email} (username: {user.username})")