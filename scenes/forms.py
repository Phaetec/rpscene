from django.conf import settings
from django.forms import ModelForm, Select
from markdownx.fields import MarkdownxFormField

from scenes.models import Scene, PlaylistItem


class SceneForm(ModelForm):
    description = MarkdownxFormField()
    characters = MarkdownxFormField()
    encounters = MarkdownxFormField()
    rewards = MarkdownxFormField()

    class Meta:
        model = Scene
        fields = ("name", "place", "description", "characters", "encounters", "rewards", "sound_effects")


class PlaylistItemForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["service"].widget = Select(choices=settings.SCENE_PLAYLIST_ACCEPTED_SERVICES)

    class Meta:
        model = PlaylistItem
        fields = ("name", "service", "uri")
