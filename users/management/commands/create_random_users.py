import random
import re
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

class Command(BaseCommand):
    help = 'Create random users with random privileges'

    def add_arguments(self, parser):
        parser.add_argument('--nb', type=int, default=5, help='Number of users to create')

    def handle(self, *args, **options):
        User = get_user_model()
        for i in range(options['nb']):
            username = f"user{i}_{get_random_string(5)}"
            email = f"{username}@example.com"
            user.first_name = re.split(r'[._-]', user.username)[0]
            user.last_name = re.split(r'[._-]', user.username)[1]
            password = "test123%"
            role = random.choices(
                ['superuser', 'staff', 'regular'],
                weights=[0.1, 0.2, 0.7],
                k=1
            )[0]

            create_fn = (
                User.objects.create_superuser if role == 'superuser'
                else User.objects.create_user
            )
            user = create_fn(
                email=email,
                username=username,
                password=password,
                is_staff=(role == 'staff'),
            )

            self.stdout.write(self.style.SUCCESS(
                f"Created {role.title()} - Username: {username}, Email: {email}"
            ))