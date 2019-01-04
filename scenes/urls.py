from django.urls import path
from scenes import views

urlpatterns = [
    path('', views.index),
]