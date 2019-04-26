from django.views.generic import TemplateView


class NameGeneratorView(TemplateView):
    template_name = "name-generator/name-generator.html"
