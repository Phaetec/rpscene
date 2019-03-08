from django.forms import Select


class SelectWithCreate(Select):
    template_name = 'scenes/widgets/select_create.html'

    def __init__(self, create_url, update_url):
        super().__init__()
        self.create_url = create_url
        self.update_url = update_url

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['create_url'] = self.create_url
        context['update_url'] = self.update_url

        print("Context!")

        return context

    # class Media:
    #     js = (static('jquery'))
