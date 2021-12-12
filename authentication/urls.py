from django.urls import path
from .views import *


urlpatterns = [
    path('register', ResgisterApiView.as_view(), name="register"),
    path('login', LoginApiView.as_view(), name="login"),
]