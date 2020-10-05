from rest_framework.routers import SimpleRouter
from to_do_backend.to_do.views import CreateUserViewSet

usersRouter = SimpleRouter()
usersRouter.register(r'api/users', CreateUserViewSet)