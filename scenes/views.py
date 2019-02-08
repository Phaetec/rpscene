from django.shortcuts import render

from .models import Scene


def index(request):
    scenes = Scene.objects.all()
    return render(request, 'scenes/index.html', {'scenes': scenes})
