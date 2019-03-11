from django.urls import path

from scenes import views

app_name = 'scenes'

urlpatterns = [
    path('', views.IndexScene.as_view(), name='index'),
    path('detail/<int:scene_id>/', views.DetailScene.as_view(), name='detail'),
    path('create/', views.CreateScene.as_view(), name='create'),
    path('edit/<int:scene_id>', views.EditScene.as_view(), name='edit'),
    path('delete/<int:scene_id>', views.DeleteScene.as_view(), name='delete'),
    path('playlist/', views.PlayListIndexScene.as_view(), name='playlist.index'),
    path('playlist/detail/<int:playlistitem_id>/', views.PlayListDetailScene.as_view(), name='playlist.detail'),
    path('playlist/create/', views.PlayListCreateScene.as_view(), name='playlist.create'),
    path('playlist/edit/<int:playlistitem_id>', views.PlayListEditScene.as_view(), name='playlist.edit'),
    path('playlist/delete/<int:playlistitem_id>', views.PlayListDeleteScene.as_view(), name='playlist.delete'),
    path('playlist/as-options/', views.PlayListOptions.as_view(), name='playlist.as-options'),
]
