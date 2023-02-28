from django.urls import path, include

from rest_framework import routers

from .views import CategoryView, BrandView

router = routers.DefaultRouter()
router.register('categories', CategoryView)
router.register('brands', BrandView)


urlpatterns = [
    
] + router.urls 
