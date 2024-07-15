from django.contrib.auth.models import User
from django.shortcuts import render
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from users_app.serializers import UserSerializer


@extend_schema_view(
    tags=["User"],
    list=extend_schema(
        summary="Получение списка зарегистрированных пользователей",
        description="Получить список зарегистрированных пользователей (Администратор)"
    ),
    retrieve=extend_schema(
        summary="Получение зарегистрированного пользователя по его ID",
        description="Получить зарегистрированного пользователя по его ID (Администратор)"
    ),
    create=extend_schema(
        summary="",
        description="This endpoint allows you to create a new user.",
    ),
    update=extend_schema(
        summary="Update an existing user",
        description="This endpoint allows you to update an existing user.",
    ),
    partial_update=extend_schema(
        summary="Partially update an existing user",
        description="This endpoint allows you to partially update an existing user.",
    ),
    destroy=extend_schema(    ),
)
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )

