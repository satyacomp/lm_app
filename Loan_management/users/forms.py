from django.forms import ModelForm
from .models import Roles, Users, Borrowers


# Roles form
class RolesForm(ModelForm):
    class Meta:
        model = Roles
        fields = "__all__"


# User forms
class SignupForm(ModelForm):
    class Meta:
        model = Users
        exclude = ["is_approved", "role_id"]


class UpdateForm(ModelForm):
    class Meta:
        model = Users
        exclude = ["password"]


class LoginForm(ModelForm):
    class Meta:
        model = Users
        exclude = ["is_approved", "role_id"]


class BorrowerForm(ModelForm):
    class Meta:
        model = Borrowers
        exclude = ["id"]
