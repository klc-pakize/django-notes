from django.urls import path
from .views import (

    #function
    home,
    student_list,
    student_create,
    student_detail,
    student_update,
    student_delete,
    studentList,
    studentDelail,
     
    #class
    StudentListCreate,
    StudentListDetail,
    StudentListGAV,
    StudentDelailGAV,

)

urlpatterns = [
    path("", home), 
    # path("student-list/", student_list),  # http://127.0.0.1:8000/api/student-list/
    # path("student-create/", student_create),  # http://127.0.0.1:8000/api/student-create/
    # path("student-detail/<int:id>", student_detail),  # http://127.0.0.1:8000/api/student-detail/id
    # path("student-update/<int:pk>", student_update),  # http://127.0.0.1:8000/api/student-update/pk
    # path("student-delete/<int:id>", student_delete),  # http://127.0.0.1:8000/api/student-delete/id
    # path("studentList", studentList),  # http://127.0.0.1:8000/api/studentList
    # path("studentDelail/<int:pk>", studentDelail),  # http://127.0.0.1:8000/api/studentDelail/pk
    
    
    #?The difference in defining the FBV and CBV endpoints is the addition of .as_view to the end.
    # path("student/", StudentListCreate.as_view()),
    # path("studentdetail/<int:pk>", StudentListDetail.as_view()),
    path("student/", StudentListGAV.as_view()),
    path("studentdetail/<int:pk>", StudentDelailGAV.as_view()),
]