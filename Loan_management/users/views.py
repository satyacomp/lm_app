# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

from .models import Roles, Users
from .forms import *


# Role Controllers
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


# User controllers
def user_login(request):
    login_form = LoginForm()
    if request.method == "POST":
        uname = request.POST["username"]
        pwd = request.POST["password"]
        user = Users.objects.get(username=uname)
        if user and user.password == pwd:
            return HttpResponse("<h3>Login is successful!</h3>")
        else:
            return HttpResponse("<h3>Invalid credentials!!</h3>")
    return render(request, "login.html", {"form": login_form})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, initial={"is_approved": 0, "role_id": 5})
        if form.is_valid():
            try:
                form.save()
                model = form.instance()
                return redirect("users_list")
            except:
                print("Error, while signup")
    else:
        form = SignupForm()
    return render(request, "signup.html", {"form": form})


def users_list(request):
    users = Users.objects.all()
    return render(request, "users_list.html", {"users": users})


def user_update(request, id):
    user = Users.objects.get(id=id)
    form = UpdateForm(
        initial={
            "id": user.id,
            "username": user.username,
            "is_approved": user.is_approved,
            "role_id": user.role_id,
        }
    )
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=user)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect("/users_list")
            except Exception as e:
                pass
    return render(request, "user_update.html", {"form": form})


def user_delete(request, id):
    user = Users.objects.get(id=id)
    try:
        user.delete()
    except:
        print("Error, while delete!!")
    return redirect("/users_list")


# Borrower controllers
def borrower_create(request, uid):
    if request.method == "POST":
        form = BorrowerForm(request.POST, initial={"user_id": uid})
        if form.is_valid():
            try:
                form.save()
                model = form.instance()
                return redirect("borrower_list")
            except:
                pass
    else:
        form = BorrowerForm()
    return render(request, "borrower_signup.html", {"form": form})


def borrowers_list(request):
    pass


def borrower_update(request, id):
    pass


def borrower_delete(request, id):
    pass


def index(request):
    return render(request, "index.html", {"user": None})
