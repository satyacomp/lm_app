from django.db import models


# Create your models here.
class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255, null=False)


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, null=False)
    role_id = models.ForeignKey("Roles", on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)


class Borrowers(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("Users", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, unique=True, null=False)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()


class User_Activity_Log(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("Users", on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100, null=False)
    description = models.TextField()
    activity_date = models.DateTimeField()
