from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from scenes.forms import SceneForm
from scenes.models import Scene


@login_required()
def index(request):
    scenes = Scene.objects.filter(owner=request.user)
    return render(request, 'scenes/index.html', {'scenes': scenes})


# TODO Check if user is allowed to see the scene
@login_required()
def detail(request, scene_id):
    scene = Scene.objects.get(id=scene_id)
    if not scene.owner == request.user:
        return redirect('error.no_access')
    return render(request, 'scenes/detail.html', {'scene': scene})


@login_required()
def create_scene(request):
    if request.method == "POST":
        pass  # TODO finish

    scene_form = SceneForm()
    return render(request, "scenes/create.html", {'form': scene_form})
