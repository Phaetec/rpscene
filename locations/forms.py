from django.forms import ModelForm, FloatField, inlineformset_factory
from markdownx.fields import MarkdownxFormField

from locations.models import Location, RaceDistribution


class LocationForm(ModelForm):
    description = MarkdownxFormField(required=False)
    history = MarkdownxFormField(required=False)

    class Meta:
        model = Location
        fields = ("name", "description", "type", "ruler", "history", "map")


class RaceDistributionForm(ModelForm):
    percentage = FloatField(min_value=0, max_value=100)

    class Meta:
        model = RaceDistribution
        fields = ("race", "percentage")


RaceDistributionFormSet = inlineformset_factory(Location, RaceDistribution, form=RaceDistributionForm,
                                                fields=("race", "percentage",), extra=1)
