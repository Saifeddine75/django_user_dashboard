from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Deletes all users from the system'

    def handle(self, *args, **options):
        verbosity = options.get('verbosity', 1)

        User = get_user_model()
        count = User.objects.count()

        confirm = input(f"Are you sure you want to delete ALL {count} users? Type 'yes' to confirm: ")
        if confirm.lower() == 'yes':
            User.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f"Successfully deleted {count} users."))
        else:
            self.stdout.write(self.style.WARNING("Aborted. No users were deleted."))