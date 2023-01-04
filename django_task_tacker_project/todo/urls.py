from django.urls import path, include

from .views import (
    todohome,

    #function view
    todolist,
    tododetail,

    #class view
    TodoListClass,
    TodoDetailClass,
    Todos,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register("todos", Todos)

urlpatterns = [
    path("", todohome),
    # path("todolist/", todolist),
    # path("tododetail/<int:pk>", tododetail)
    
    # path("todoList/", TodoListClass.as_view()),
    # path("todoList/<int:pk>", TodoDetailClass.as_view()),
    path("", include(router.urls))
]