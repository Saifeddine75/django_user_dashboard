from django import forms
from .models import Users


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ("email", "name")


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ("name", "email")
