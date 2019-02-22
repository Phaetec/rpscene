from django.shortcuts import render


# TODO Add a real index html instead of the base
def index(request):
    return render(request, 'base.html', {})


def no_access(request, exception=None):
    return render(request, 'errors/no_access.html', {})
