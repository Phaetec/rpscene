from django.urls import include, path

from . import views

app_name = 'characters'
urlpatterns = [
    path('', views.index, name='index'),
    path('name-generator', include('characters.name_generator.urls', namespace='name-generator'))
]
