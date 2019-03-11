from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from locations.forms import LocationForm
from locations.models import Location
from utils.mixins.AjaxTemplateMixin import AjaxTemplateMixin
from utils.mixins.UserIsOwnerMixin import UserIsOwnerMixin


class IndexLocation(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'locations/index.html'
    context_object_name = 'locations'
    paginate_by = 5

    def get_queryset(self):
        return Location.objects.filter(owner=self.request.user)


class IndexOptionsLocation(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'locations/indexoptions.html'
    context_object_name = 'locations'


class DetailLocation(LoginRequiredMixin, UserIsOwnerMixin, DetailView):
    model = Location
    pk_url_kwarg = 'location_id'
    template_name = 'locations/detail.html'


class CreateLocation(LoginRequiredMixin, AjaxTemplateMixin, CreateView):
    model = Location
    form_class = LocationForm
    pk_url_kwarg = 'location_id'
    template_name = 'locations/create.html'
    ajax_template_name = 'locations/create_inner.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('locations:detail', kwargs={'location_id': self.object.id})


class EditLocation(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Location
    form_class = LocationForm
    pk_url_kwarg = 'location_id'
    template_name = 'locations/edit.html'

    def get_success_url(self):
        return reverse_lazy('locations:detail', kwargs={'location_id': self.object.id})


class DeleteLocation(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Location
    pk_url_kwarg = 'location_id'
    template_name = 'locations/delete.html'
    success_url = reverse_lazy('locations:index')
