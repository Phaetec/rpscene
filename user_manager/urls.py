from django.urls import path

from . import views

app_name = "user_manager"

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup")
]
