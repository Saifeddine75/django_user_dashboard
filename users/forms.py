from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ["email"]

    def save(self, commit=True):
        user = super().save(commit=False)

        # Generate username from email
        raw = self.cleaned_data['email']
        base = raw.split('@')[0]
        base = re.split(r'[._-]', base)[0]

        if commit:
            user.save()
            print(f"User {self.email} saved successfully.")

        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Users
        exclude = ["is_superuser", "email"]
