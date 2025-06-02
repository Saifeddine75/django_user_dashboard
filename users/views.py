from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Users
from .forms import CustomUserCreationForm, CustomUserChangeForm


# Create your views here.
class UserCreateView(CreateView):
    model = Users
    form_class = CustomUserCreationForm
    template_name = "users/user_create.html"
    success_url = reverse_lazy("user-list")  # Redirect to user list after creation


class UserListView(ListView):
    model = Users
    template_name = "users/user_list.html"
    context_object_name = "users"  # Name of the variable to access in the template

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")  # récupération du paramètre 'q' dans l'URL
        if query:
            queryset = queryset.filter(name__icontains=query)
        return queryset


class UserUpdateView(UpdateView):
    model = Users
    form_class = CustomUserChangeForm  # form for updating users
    template_name = "users/user_update.html"
    success_url = reverse_lazy("user-list")


class UserDeleteView(DeleteView):
    model = Users
    template_name = "users/user_confirm_delete.html"
    success_url = reverse_lazy("user-list")
