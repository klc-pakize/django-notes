from django.urls import path, include

from rest_framework import routers

from .views import BlogMVS, CategoryMVS

router = routers.DefaultRouter()
router.register("blog", BlogMVS)
router.register("category", CategoryMVS)

urlpatterns = [
    path("",include(router.urls))
]
