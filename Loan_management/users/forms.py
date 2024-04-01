from django.forms import ModelForm
from .models import Roles, Users
from django import forms


class RolesForm(ModelForm):
    class Meta:
        model = Roles
        fields = "__all__"


class SignupForm(ModelForm):
    class Meta:
        model = Users
        fields = "__all__"


class LoginForm(forms.Form):
    pass
