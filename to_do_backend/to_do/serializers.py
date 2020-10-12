from rest_framework import serializers
from django.contrib.auth.models import User
from to_do_backend.to_do.models import ToDo
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'priority', 'complited']
        validators = []

    def create(self, validated_data):
        current_user = self.context['request'].user
        toDo = ToDo(**validated_data, user=current_user)
        toDo.save()
        return toDo
