from django.contrib.auth import get_user_model
User = get_user_model()

# Don't forget to set up your environment variables with your email

User.objects.create_superuser(
    email=os.environ.get('EMAIL_ACCOUNT_1'),
    username='admin',
    password='test123%'
)

User.objects.create_user(
    email=os.environ.get('EMAIL_ACCOUNT_2'),
    username='staff',
    password='test123%',
    is_staff=True,
    is_superuser=False
)

User.objects.create_user(
    email=os.environ.get('EMAIL_ACCOUNT_3'),
    username='user',
    password='test123%',
    is_staff=False,
    is_superuser=False
)