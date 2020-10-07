from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from to_do_backend.to_do.serializers import UserSerializer, UserDetailSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from to_do_backend.to_do.models import ToDo
from to_do_backend.to_do.serializers import ToDoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

# Create your views here.


class CreateUserViewSet(viewsets.GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserDetailViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)


# class CreateUserViewSet(viewsets.ModelViewSet, CreateModelMixin):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     http_method_names = ['post']
#     permission_classes = [permissions.AllowAny]


class ToDoViewSet(viewsets.ModelViewSet, RetrieveModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(user=user)



