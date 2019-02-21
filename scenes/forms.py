from django.forms import ModelForm
from markdownx.fields import MarkdownxFormField

from scenes.models import Scene


class SceneForm(ModelForm):
    description = MarkdownxFormField()
    place = MarkdownxFormField()

    class Meta:
        model = Scene
        fields = ("name", "description", "place", "characters", "rewards", "encounters")
