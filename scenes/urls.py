from django.urls import path

from scenes import views

app_name = 'scenes'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:scene_id>/', views.detail, name='detail'),
    path('create/', views.create_scene, name='create'),
]
