from django.shortcuts import render

from .models import Scene


def index(request):
    scenes = Scene.objects.all()
    return render(request, 'scenes/index.html', {'scenes': scenes})


# TODO Check if user is allowed to see the scene
def detail(request, scene_id):
    scene = Scene.objects.get(id=scene_id)
    return render(request, 'scenes/detail.html', {'scene': scene})
