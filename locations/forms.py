from django.forms import FloatField, ModelForm, inlineformset_factory
from markdownx.fields import MarkdownxFormField

from locations.models import Location, RaceDistribution
from utils.widgets.fancybulmafileinput import FancyBulmaFileInput


class LocationForm(ModelForm):
    description = MarkdownxFormField(required=False)
    history = MarkdownxFormField(required=False)

    description.widget.attrs['class'] = 'textarea'
    history.widget.attrs['class'] = 'textarea'

    class Meta:
        model = Location
        fields = ("name", "description", "type", "ruler", "history", "map")

        widgets = {'map': FancyBulmaFileInput()}


class RaceDistributionForm(ModelForm):
    percentage = FloatField(min_value=0, max_value=100)

    class Meta:
        model = RaceDistribution
        fields = ("race", "percentage")


RaceDistributionFormSet = inlineformset_factory(Location, RaceDistribution, form=RaceDistributionForm,
                                                fields=("race", "percentage",), extra=1)
