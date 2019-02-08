from django.shortcuts import render


# TODO Add a real index html instead of the base
def index(request):
    return render(request, 'base.html', {})
