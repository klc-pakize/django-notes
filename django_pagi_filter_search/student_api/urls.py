from django.urls import path, include
from .views import (
    home,
    StudentMVS,
    PathMVS,
)

from rest_framework import routers

router = routers.DefaultRouter()
router.register("student", StudentMVS)
router.register("path", PathMVS)

urlpatterns = [
    path("", home), 
    path("",include(router.urls))
]