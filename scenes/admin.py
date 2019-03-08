from django.contrib import admin

# Register your models here.
from scenes.models import Scene, PlaylistItem

admin.site.register(Scene)
admin.site.register(PlaylistItem)
