# Create your views here.
from django.shortcuts import render
import collections
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404


class RolesApiView(APIView):

    renderer_classes = [TemplateHTMLRenderer]

    def get_object(self, id):
        return get_object_or_404(self.get_queryset(), id=id)

    def get_queryset(self, *args, **kwargs):
        roles = Roles.objects.all()
        return roles

    # 1. Get roles all or by id
    def get(self, request, id=None, *args, **kwargs):
        id = id or request.query_params.get("id")
        data = []
        if id:
            serializer = RolesSerializer(self.get_object(id))
            data.append(serializer.data)
            return Response({"roles": data}, template_name="roles.html")
        else:
            serializer = RolesSerializer(self.get_queryset(), many=True)
            return Response({"roles": serializer.data}, template_name="roles.html")

    # 2. Post roles
    def post(self, request):
        role_serializer = RolesSerializer(data=request.data)
        if role_serializer.is_valid():
            role_serializer.save()
            return Response(role_serializer.data, status=status.HTTP_201_CREATED)
        return Response(role_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 3. Put role
    def put(self, request, id=None, format=None):
        role = self.get_object(id)
        role_serializer = RolesSerializer(role, data=request.data)
        if role_serializer.is_valid():
            role_serializer.save()
            return Response(role_serializer.data)
        return Response(role_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 4. Delete role
    def delete(self, request, id=None, format=None):
        role = self.get_object(id)
        role.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UsersApiView(APIView):
    # 1. Get all users
    def get(self, request, *args, **kwargs):
        pass


# First rendering file
def index(request):
    return render(request, "index.html")


# User signup
def signup(request):
    return render(request, "signup.html")
