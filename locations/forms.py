from django.forms import ModelForm
from markdownx.fields import MarkdownxFormField

from locations.models import Location


class LocationForm(ModelForm):
    description = MarkdownxFormField(required=False)
    history = MarkdownxFormField(required=False)

    class Meta:
        model = Location
        fields = ("name", "description", "type", "ruler", "history", "map")
