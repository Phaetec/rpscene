from django.urls import path

from locations import views

app_name = 'locations'

urlpatterns = [
    path('', views.IndexLocation.as_view(), name='index'),
    path('detail/<int:location_id>/', views.DetailLocation.as_view(), name='detail'),
    path('create/', views.CreateLocation.as_view(), name='create'),
    path('edit/<int:location_id>', views.EditLocation.as_view(), name='edit'),
    path('delete/<int:location_id>', views.DeleteLocation.as_view(), name='delete'),
]
