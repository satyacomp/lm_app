from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    # roles end points
    path("roles_list", views.roles_list, name="roles_list"),
    path("role_create", views.role_create, name="role_create"),
    path("role_update/<int:id>", views.role_update, name="role_update"),
    path("role_delete/<int:id>", views.role_delete, name="role_delete"),
    # Users end points
    path("login", views.user_login, name="login"),
    path("user_signup", views.signup, name="user_signup"),
    path("users_list", views.users_list, name="users_list"),
    path("user_update/<int:id>", views.user_update, name="user_update"),
    path("user_delete/<int:id>", views.user_delete, name="user_delete"),
    # Borrowers end points
    path("borrower/<int:uid>", views.borrower_create, name="borrower_signup"),
]
