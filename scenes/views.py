from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

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
    scene_form = None

    if request.method == "POST":
        scene_form = SceneForm(request.POST)
        if scene_form.is_valid():
            scene = scene_form.save(commit=False)
            scene.owner = request.user
            scene.save()

    if scene_form is None:
        scene_form = SceneForm()

    return render(request, "scenes/create.html", {'form': scene_form})
