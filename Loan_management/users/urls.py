from django.urls import path
from . import views

urlpatterns = [
    path("roles_list", views.roles_list, name="roles_list"),
    path("role_create", views.role_create, name="role_create"),
    path("role_update/<int:id>", views.role_update, name="role_update"),
    path("role_delete/<int:id>", views.role_delete, name="role_update"),
    path("user_signup", views.signup, name="user_signup"),
    path("users_list", views.users_list, name="users_list"),
]
