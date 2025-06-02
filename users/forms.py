
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Users

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ('email', 'name') 

    def get_queryset(request, name):
        user = Users.objects.filter(name=name)