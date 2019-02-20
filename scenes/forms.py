from django import forms
from markdownx.fields import MarkdownxFormField


class SceneForm(forms.Form):
    description = MarkdownxFormField()
    place = MarkdownxFormField()
