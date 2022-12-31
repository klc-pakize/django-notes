from django.urls import path
from .views import (
    home,
    student_list,
    student_create,
    student_detail,
    student_update,
    student_delete
)

urlpatterns = [
    path("", home), 
    path("student-list/", student_list),  # http://127.0.0.1:8000/api/student-list/
    path("student-create/", student_create),  # http://127.0.0.1:8000/api/student-create/
    path("student-detail/<int:id>", student_detail),  # http://127.0.0.1:8000/api/student-detail/id
    path("student-update/<int:pk>", student_update),  # http://127.0.0.1:8000/api/student-update/pk
    path("student-delete/<int:id>", student_delete),  # http://127.0.0.1:8000/api/student-delete/id

]