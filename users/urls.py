from django.urls import path
from .views import UserListView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("new/", UserCreateView.as_view(), name="user-create"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="user-update"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),
]
