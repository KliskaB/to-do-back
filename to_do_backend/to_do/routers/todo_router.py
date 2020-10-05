from rest_framework.routers import SimpleRouter
from to_do_backend.to_do.views import ToDoViewSet

toDoRouter = SimpleRouter()
toDoRouter.register(r'api/todos', ToDoViewSet)