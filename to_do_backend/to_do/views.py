from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from to_do_backend.to_do.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from to_do_backend.to_do.models import ToDo
from to_do_backend.to_do.serializers import ToDoSerializer

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

class ToDoViewSet(viewsets.ModelViewSet, RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user)



