from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Users
from .forms import CustomUserCreationForm

# Create your views here.
class UserCreateView(CreateView):
    model = Users
    form_class = CustomUserCreationForm
    template_name = 'users/user_create.html'

class UserListView(ListView):
    model = Users
    template_name = 'users/user_list.html'

