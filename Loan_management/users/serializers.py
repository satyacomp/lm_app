from rest_framework import serializers
from .models import *


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowers
        fields = "__all__"


class UserActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowers
        fields = "__all__"
