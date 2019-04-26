from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from characters.forms import CharacterForm
from .models import Character


# Create your views here.
class IndexCharacters(LoginRequiredMixin, ListView):
    model = Character
    template_name = 'characters/list.html'


class CreateCharacter(LoginRequiredMixin, CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'characters/create.html'
    success_url = reverse_lazy("characters:index")
