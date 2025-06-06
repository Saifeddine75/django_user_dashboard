from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Users
# from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


USER_ATTRIBUTES = [
    ("Email", "email"),
    ("Username", "username"),
    ("First name", "first_name"),
    ("Last name", "last_name"),
    ("Updated at", "updated_at"),
]


class UserCreateView(CreateView):
    model = Users
    form_class = CustomUserCreationForm
    template_name = "users/user_create.html"
    success_url = reverse_lazy("user-list")  # Redirect to user list after creation


class UserListView(ListView):
    model = Users
    template_name = "users/user_list.html"
    context_object_name = "users"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = Users.objects.all()  # Fetch all users from the User model

        users_with_attrs = []
        for user in users:
            attrs = []
            for label, attr in USER_ATTRIBUTES:
                value = getattr(user, attr, None)
                if value not in [None, '']:
                    attrs.append((label, value))
            users_with_attrs.append({"user": user, "attributes": attrs})

        context["users_with_attrs"] = users_with_attrs
        return context


class UserUpdateView(UpdateView):
    model = Users
    form_class = CustomUserChangeForm  # form for updating users
    template_name = "users/user_update.html"
    success_url = reverse_lazy("user-list")


class UserDeleteView(DeleteView):
    model = Users
    template_name = "users/user_confirm_delete.html"
    success_url = reverse_lazy("user-list")
