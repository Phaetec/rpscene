from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from encounters.forms import DnD5eNPCForm, DnD5eActionFormSet, DnD5eSpecialAbilityFormSet, DnD5eLairActionFormSet, \
    DnD5eLegendaryActionFormSet
from encounters.models import DnD5eNPC


class Create5eNPC(LoginRequiredMixin, CreateView):
    """
    Create a new Dungeons & Dragons 5th Edition NPC.
    """
    model = DnD5eNPC
    form_class = DnD5eNPCForm
    template_name = 'encounters/npcs/create_dnd_5e_npc.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["actions"] = DnD5eActionFormSet(self.request.POST)
            data["special_abilities"] = DnD5eSpecialAbilityFormSet(self.request.POST)
            data["legendary_actions"] = DnD5eLegendaryActionFormSet(self.request.POST)
            data["lair_actions"] = DnD5eLairActionFormSet(self.request.POST)
        else:
            data["actions"] = DnD5eActionFormSet()
            data["special_abilities"] = DnD5eSpecialAbilityFormSet()
            data["legendary_actions"] = DnD5eLegendaryActionFormSet()
            data["lair_actions"] = DnD5eLairActionFormSet()
        return data

    def get_success_url(self):
        return reverse_lazy('encounters:npc.5e')


class IndexDnD5eNPC(LoginRequiredMixin, ListView):
    """
    List all available Dungeons & Dragons 5th Edition NPCs.
    """
    model = DnD5eNPC
    template_name = 'encounters/npcs/index_dnd_5e.html'
    context_object_name = 'npcs'
