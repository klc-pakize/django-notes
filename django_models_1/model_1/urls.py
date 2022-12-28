from django.urls import path
from .views import home


urlpatterns = [
 path("home",home)   # http://127.0.0.1:8000/model_1/home  If we write it, it will show us the HttpResponse browser that we have written to the home function.
]