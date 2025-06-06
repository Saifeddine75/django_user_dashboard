import re
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
        user.username = raw.split('@')[0]
        try:
            user.first_name = re.split(r'[._-]', user.username)[0]
            user.last_name = re.split(r'[._-]', user.username)[1]
        except Exception as e:
            print("Error while parsing user info:")
            print(f"Raw input: {raw}")
            print("Exception:", e)
            

        if commit:
            user.save()
            print(f"User {self.email} saved successfully.")

        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Users
        fields = ['groups', 'user_permissions', 'is_staff', 'is_active']