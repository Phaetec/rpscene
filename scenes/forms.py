from django.forms import ModelForm
from markdownx.fields import MarkdownxFormField

from scenes.models import Scene


class SceneForm(ModelForm):
    description = MarkdownxFormField()

    class Meta:
        model = Scene
        fields = ("name", "place", "description", "characters", "encounters", "rewards")
