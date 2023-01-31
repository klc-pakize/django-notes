from django.urls import path

from .views import DepartmentView

urlpatterns = [
    path("department/", DepartmentView().as_view()),
]
