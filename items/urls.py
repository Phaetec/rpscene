from django.urls import path

from . import views

urlpatterns = [
    path('armory/', views.armory, name='armory'),
]
