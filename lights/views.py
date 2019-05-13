from django.shortcuts import render


# Create your views here.
def test(request):
    return render(request, 'lights/test.html', {})


def hue_pair(request):
    """
    Pairs your bridge with the app.

    :param request: Django Request
    :return: Homepage where user can pair their bridge.
    """
    return render(request, 'lights/pairing.html')
