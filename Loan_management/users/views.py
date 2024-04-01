# Create your views here.
from django.shortcuts import redirect, render

from .models import Roles, Users
from .forms import RolesForm, SignupForm


# creating views for roles
def roles_list(request):
    roles = Roles.objects.all()
    return render(request, "roles_list.html", {"roles": roles})


def role_create(request):
    if request.method == "POST":
        form = RolesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance()
                return redirect("roles_list")
            except:
                pass
    else:
        form = RolesForm()
    return render(request, "role_create.html", {"form": form})


def role_update(request, id):
    role = Roles.objects.get(id=id)
    form = RolesForm(initial={"role_name": role.role_name})
    if request.method == "POST":
        form = RolesForm(request.POST, instance=role)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect("/roles_list")
            except Exception as e:
                pass
    return render(request, "role_update.html", {"form": form})


def role_delete(request, id):
    role = Roles.objects.get(id=id)
    try:
        role.delete()
    except:
        pass
    return redirect("/roles_list")


# User actions/routes
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance()
                return redirect("users_list")
            except:
                pass
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})


def users_list(request):
    pass
