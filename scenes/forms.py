from django.conf import settings
from django.forms import ModelForm, Select
from django.templatetags.static import static
from django.urls import reverse_lazy
from markdownx.fields import MarkdownxFormField

from scenes.models import PlaylistItem, Scene


class SceneForm(ModelForm):
    description = MarkdownxFormField()
    characters = MarkdownxFormField()
    encounters = MarkdownxFormField()
    rewards = MarkdownxFormField()

    class Meta:
        model = Scene
        fields = ("name", "place", "description", "characters", "encounters", "rewards", "sound_effects")

        widgets = {
            'place': Select(attrs={
                "create-url": reverse_lazy("locations:create"),
                "update-url": reverse_lazy("locations:as-options"),
                "select-with-create": ""
            })
        }

    class Media:
        js = (static('node_modules/jquery/dist/jquery.js'),
              static('js/rpscene.js'))


class PlaylistItemForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["service"].widget = Select(choices=settings.SCENE_PLAYLIST_ACCEPTED_SERVICES)

    class Meta:
        model = PlaylistItem
        fields = ("name", "service", "uri")
