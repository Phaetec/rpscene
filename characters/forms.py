from django.forms import ModelForm

from characters.models import Character


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        exclude = ("user",)
