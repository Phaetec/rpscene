from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from lights.models import HuePair


def test(request):
    return render(request, 'lights/test.html', {})


@login_required()
def hue_pair(request):
    """
    Pairs your bridge with the app.

    :param request: Django Request
    :return: Homepage where user can pair their bridge.
    """
    return render(request, 'lights/pairing.html')


@require_POST
@login_required()
def save_successful_pair(request):
    """
    Saves the key resulting from a pairing to the hue Bridge.
    Only accessable via AJAX. Request must contain `bridge_name` variable containing the key.

    :param request:
    :return:
    """
    if not request.is_ajax():
        return HttpResponseNotFound("There is nothing here for mere mortals.")

    hue_key = request.POST.get("bridge_name")
    if hue_key is None:
        return JsonResponse(data={"text": "The pairing failed, try again."},
                            status=500)

    try:
        old_key = HuePair.objects.get(user=request.user)
        old_key.hue_key = hue_key
        old_key.save()
    except HuePair.DoesNotExist:
        key = HuePair(user=request.user, hue_key=hue_key)
        key.save()

    return JsonResponse(data={"text": "Successfully created the pairing."}, status=200)


def hue_scene(request):
    return render(request, "base.html", {})
