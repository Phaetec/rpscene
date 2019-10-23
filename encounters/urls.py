from django.urls import path

from . import views

app_name = 'encounters'
urlpatterns = [
    path('create/', views.CreateEncounter.as_view(), name='create'),
    path('npcs/5e/', views.IndexDnD5eNPC.as_view(), name='npc.5e'),
    path('npcs/5e/<int:npc_id>', views.DetailDnD5eNPC.as_view(), name='npc.5e.detail'),
    path('npcs/add/5e/', views.Create5eNPC.as_view(), name='npc.5e.add'),
]
