from django.urls import path, include
from rest_framework import routers
from .views import  DepartmentMVS, PersonMVS, department_detail, department_list



router = routers.DefaultRouter()
router.register("person", PersonMVS)
router.register("", DepartmentMVS)


urlpatterns = [
    path("", include(router.urls)),
    path("department", department_list),
    path("department/<str:name>", department_detail)
]
