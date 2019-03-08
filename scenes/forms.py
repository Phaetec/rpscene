from django.conf import settings
from django.forms import ModelForm, Select
from django.urls import reverse_lazy
from markdownx.fields import MarkdownxFormField

from scenes.models import PlaylistItem, Scene
from utils.widgets.select_with_create import SelectWithCreate


class SceneForm(ModelForm):
    description = MarkdownxFormField()
    characters = MarkdownxFormField()
    encounters = MarkdownxFormField()
    rewards = MarkdownxFormField()

    class Meta:
        model = Scene
        fields = ("name", "place", "description", "characters", "encounters", "rewards", "sound_effects")

        create_url = reverse_lazy("locations:create")
        update_url = reverse_lazy("locations:as-options")
        widgets = {
            'place': SelectWithCreate(create_url, update_url)
        }


class PlaylistItemForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["service"].widget = Select(choices=settings.SCENE_PLAYLIST_ACCEPTED_SERVICES)

    class Meta:
        model = PlaylistItem
        fields = ("name", "service", "uri")
