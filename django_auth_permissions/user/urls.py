from django.urls import path
from .views import RegisterView

from rest_framework.authtoken import views

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path('login/', views.obtain_auth_token)  #! Until this process, there was no automatic token generation for the user, thanks to this process, automatic token will be generated when the user is logged in.
]