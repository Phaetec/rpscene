from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from encounters.forms import DnD5eNPCForm
from encounters.models import DnD5eNPC


class Create5eNPC(LoginRequiredMixin, CreateView):
    """
    Create a new Dungeons & Dragons 5th Edition NPC.
    """
    model = DnD5eNPC
    form_class = DnD5eNPCForm
    template_name = 'encounters/npcs/create_dnd_5e_npc.html'


class IndexDnD5eNPC(LoginRequiredMixin, ListView):
    """
    List all available Dungeons & Dragons 5th Edition NPCs.
    """
    model = DnD5eNPC
    template_name = 'encounters/npcs/index_dnd_5e.html'
    context_object_name = 'npcs'

    @staticmethod
    def get_success_url():
        return reverse_lazy('encounters:npc.5e')
