from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from utils.logger import get_logger

from .models import Users
# from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

logger = get_logger(__name__)


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

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            logger.debug(f"Filtering users with query: {query}")
            queryset = queryset.filter(
                Q(username__icontains=query) |
                Q(email__icontains=query) |
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )
        if self.request.GET.get('is_admin') == '1':
            queryset = queryset.filter(is_staff=True)
        if self.request.GET.get('is_active') == '1':
            queryset = queryset.filter(is_active=True)
        
        logger.debug(f"Number of matched User: {queryset.count()}")
        for user in queryset:
            logger.debug(f"Matched User: {user.username} | {user.email} | {user.first_name} {user.last_name}")

        return queryset
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users_queryset = self.get_queryset()
        context['query'] = self.request.GET.get('q', '')
        context['is_admin'] = self.request.GET.get('is_admin', '')
        context['is_active'] = self.request.GET.get('is_active', '')
        context['users_count'] = users_queryset.count()

        users_with_attrs = []
        for user in users_queryset:
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
