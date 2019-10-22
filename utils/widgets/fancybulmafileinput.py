from pathlib import Path

from django.forms.widgets import CheckboxInput, Input
from django.utils.translation import gettext_lazy as _

FILE_INPUT_CONTRADICTION = object()


class FancyBulmaFileInput(Input):
    """Custom Bulma File input based on FileInput/ClearableFileInput.
    A custom class not based on FileInput and ClearableFileInput is necessary
    to prevent the bulma form filter from modifying this element."""
    input_type = 'file'
    needs_multipart_form = True
    clear_checkbox_label = _('Clear')
    choose_file_label = _('Choose a file')
    initial_text = _('Currently')
    input_text = _('Change')
    template_name = 'fancybulmafileinput/file_input.html'

    def clear_checkbox_name(self, name):
        """
        Given the name of the file input, return the name of the clear checkbox
        input.
        """
        return name + '-clear'

    def clear_checkbox_id(self, name):
        """
        Given the name of the clear checkbox input, return the HTML id for it.
        """
        return name + '_id'

    def is_initial(self, value):
        """
        Return whether value is considered to be initial value.
        """
        return bool(value and getattr(value, 'url', False))

    def format_value(self, value):
        """
        Return the file object if it has a defined url attribute.
        """
        if self.is_initial(value):
            return value

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        checkbox_name = self.clear_checkbox_name(name)
        checkbox_id = self.clear_checkbox_id(checkbox_name)
        uploaded_file_name = Path(str(value)).name
        context['widget'].update({
            'checkbox_name': checkbox_name,
            'checkbox_id': checkbox_id,
            'is_initial': self.is_initial(value),
            'input_text': self.input_text,
            'initial_text': self.initial_text,
            'clear_checkbox_label': self.clear_checkbox_label,
            'choose_file_label': self.choose_file_label,
            'uploaded_file_name': uploaded_file_name,
        })
        return context

    def value_from_datadict(self, data, files, name):
        upload = files.get(name)
        if not self.is_required and CheckboxInput().value_from_datadict(
                data, files, self.clear_checkbox_name(name)):

            if upload:
                # If the user contradicts themselves (uploads a new file AND
                # checks the "clear" checkbox), we return a unique marker
                # object that FileField will turn into a ValidationError.
                return FILE_INPUT_CONTRADICTION
            # False signals to clear any existing value,
            # as opposed to just None
            return False
        return upload

    def use_required_attribute(self, initial):
        return super().use_required_attribute(initial) and not initial

    def value_omitted_from_data(self, data, files, name):
        return (
                name not in files and
                self.clear_checkbox_name(name) not in data
        )
