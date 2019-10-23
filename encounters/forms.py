from django.forms import ModelForm, inlineformset_factory

from encounters.models import DnD5eNPC, DnD5eAction, DnD5eSpecialAbility, DnD5eLegendaryAction, DnD5eLairAction


class DnD5eNPCForm(ModelForm):
    class Meta:
        model = DnD5eNPC
        exclude = ('owner',)


class DnD5eActionForm(ModelForm):
    class Meta:
        model = DnD5eAction
        exclude = ('npc',)


class DnD5eSpecialAbilityForm(ModelForm):
    class Meta:
        model = DnD5eSpecialAbility
        exclude = ('npc',)


class DnD5eLegendaryActionForm(ModelForm):
    class Meta:
        model = DnD5eLegendaryAction
        exclude = ('npc',)


class DnD5eLairActionForm(ModelForm):
    class Meta:
        model = DnD5eLairAction
        exclude = ('npc',)


DnD5eActionFormSet = inlineformset_factory(DnD5eNPC, DnD5eAction, form=DnD5eActionForm, fields=("name", "description",),
                                           extra=1)

DnD5eSpecialAbilityFormSet = inlineformset_factory(DnD5eNPC, DnD5eSpecialAbility, form=DnD5eSpecialAbilityForm,
                                                   fields=("name", "description",), extra=1)

DnD5eLegendaryActionFormSet = inlineformset_factory(DnD5eNPC, DnD5eLegendaryAction, form=DnD5eLegendaryActionForm,
                                                    fields=("name", "description",), extra=1)

DnD5eLairActionFormSet = inlineformset_factory(DnD5eNPC, DnD5eLairAction, form=DnD5eLairActionForm,
                                               fields=("name", "description",), extra=1)
