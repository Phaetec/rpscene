from django.urls import path

from characters.name_generator import views

app_name = 'name-generator'
urlpatterns = [
    path('', views.NameGeneratorView.as_view(), name='index'),
]
