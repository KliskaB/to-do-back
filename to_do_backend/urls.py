"""to_do_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from to_do_backend.to_do.routers.user_router import usersRouter
from to_do_backend.to_do.routers.todo_router import toDoRouter
from to_do_backend.to_do.views import UserDetailViewSet

router = routers.DefaultRouter()
# router.register(r'api/users', views.CreateUserViewSet)
router.registry.extend(usersRouter.registry)
router.registry.extend(toDoRouter.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/me/', UserDetailViewSet.as_view(), name='users_me'),
    path('api/users/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
