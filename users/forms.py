
from django import forms
from .models import Users

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('email', 'name') 

    def get_queryset(request, name):
        user = Users.objects.filter(name=name)