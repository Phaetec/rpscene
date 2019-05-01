from django.urls import include, path

from . import views

app_name = 'characters'
urlpatterns = [
    path('', views.IndexCharacters.as_view(), name='index'),
    path('create', views.CreateCharacter.as_view(), name='create'),
]
