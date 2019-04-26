from django.forms import ModelForm, inlineformset_factory

from encounters.models import DnD5eNPC, DnD5eAction


class DnD5eNPCForm(ModelForm):
    class Meta:
        model = DnD5eNPC
        exclude = ()


class DnD5eActionForm(ModelForm):
    class Meta:
        model = DnD5eAction
        exclude = ('npc',)


DnD5eActionFormSet = inlineformset_factory(DnD5eNPC, DnD5eAction, form=DnD5eActionForm, fields=("name", "description",),
                                           extra=1)
