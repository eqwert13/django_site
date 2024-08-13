from django.urls import path
from .views import register

app_name = "users"  # namespace


urlpatterns = [
    # http://127.0.0.1:8000/users/
    path("register/", register, name="register"),
]
