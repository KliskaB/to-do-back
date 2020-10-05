from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.mixins import CreateModelMixin
from to_do_backend.to_do.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

# Create your views here.

class CreateUserViewSet(viewsets.GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# class CreateUserViewSet(viewsets.ModelViewSet, CreateModelMixin):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     http_method_names = ['post']
#     permission_classes = [permissions.AllowAny]


