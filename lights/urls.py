from django.urls import path

from lights import views

app_name = 'lights'

urlpatterns = [
    path('test/', views.test, name="test"),
    path('pairing/', views.hue_pair, name="hue.pairing"),
]
