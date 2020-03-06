from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from encounters.forms import DnD5eNPCForm, DnD5eActionFormSet, DnD5eSpecialAbilityFormSet, DnD5eLairActionFormSet, \
    DnD5eLegendaryActionFormSet, EncounterForm, DnDEncounterFormSet
from encounters.models import DnD5eNPC, Encounter
from utils.mixins.UserIsOwnerMixin import UserIsOwnerMixin


class CreateEncounter(LoginRequiredMixin, CreateView):
    """
    Create a new Encounter
    """
    model = Encounter
    form_class = EncounterForm
    template_name = 'encounters/create_encounter.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["npcs"] = DnDEncounterFormSet(self.request.POST)
        else:
            data["npcs"] = DnDEncounterFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        with transaction.atomic():
            form.instance.owner = self.request.user
            self.object = form.save()
            npcs = context["npcs"]
            if npcs.is_valid():
                npcs.instance = self.object
                npcs.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('encounters:create')


class EncounterIndex(LoginRequiredMixin, ListView):
    model = Encounter
    template_name = "encounters/index.html"
    context_object_name = "encounters"


class EncounterDetail(LoginRequiredMixin, DetailView):
    model = Encounter
    pk_url_kwarg = 'encounter_id'
    context_object_name = 'encounter'
    template_name = 'encounters/detail.html'


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

    def form_valid(self, form):
        context = self.get_context_data()
        actions = context["actions"]
        special_abilities = context["special_abilities"]
        legendary_actions = context["legendary_actions"]
        lair_actions = context["lair_actions"]
        with transaction.atomic():
            form.instance.owner = self.request.user
            self.object = form.save()
            if actions.is_valid():
                actions.instance = self.object
                actions.save()
            if special_abilities.is_valid():
                special_abilities.instance = self.object
                special_abilities.save()
            if legendary_actions.is_valid():
                legendary_actions.instance = self.object
                legendary_actions.save()
            if lair_actions.is_valid():
                lair_actions.instance = self.object
                lair_actions.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('encounters:npc.5e')


class IndexDnD5eNPC(LoginRequiredMixin, ListView):
    """
    List all available Dungeons & Dragons 5th Edition NPCs.
    """
    model = DnD5eNPC
    template_name = 'encounters/npcs/index_dnd_5e.html'
    context_object_name = 'npcs'


class DetailDnD5eNPC(LoginRequiredMixin, UserIsOwnerMixin, DetailView):
    model = DnD5eNPC
    pk_url_kwarg = 'npc_id'
    context_object_name = 'npc'
    template_name = 'encounters/npcs/details.html'
