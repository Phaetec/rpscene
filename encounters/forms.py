from django.forms import ModelForm

from encounters.models import DnD5eNPC


class DnD5eNPCForm(ModelForm):
    class Meta:
        model = DnD5eNPC
        exclude = ()
