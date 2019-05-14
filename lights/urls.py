from django.urls import path

from lights import views

app_name = 'lights'

urlpatterns = [
    path('test/', views.test, name="test"),
    path('pairing/', views.hue_pair, name="hue.pairing"),
    path('pairing/save/', views.save_successful_pair, name="hue.pairing.save"),
    path('hue/scene/', views.hue_scene, name="hue.scene"),
]
