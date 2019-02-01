from django.shortcuts import render
from .models import Character


# Create your views here.
def index(request):
    all_chars = Character.objects.all()
    return render(request, 'characters/list.html', {'chars': all_chars})
