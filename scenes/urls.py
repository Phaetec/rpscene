from django.urls import path

from scenes import views

app_name = 'scenes'

urlpatterns = [
    path('', views.IndexScene.as_view(), name='index'),
    path('detail/<int:scene_id>/', views.DetailScene.as_view(), name='detail'),
    path('create/', views.CreateScene.as_view(), name='create'),
    path('edit/<int:scene_id>', views.EditScene.as_view(), name='edit'),
    path('delete/<int:scene_id>', views.DeleteScene.as_view(), name='delete'),
]
