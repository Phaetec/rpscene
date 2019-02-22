from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from scenes.forms import SceneForm
from scenes.models import Scene


class UserIsOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user == self.get_object().owner


class IndexScene(LoginRequiredMixin, ListView):
    model = Scene
    template_name = 'scenes/index.html'
    context_object_name = 'scenes'
    paginate_by = 5

    def get_queryset(self):
        return Scene.objects.filter(owner=self.request.user)


class DetailScene(LoginRequiredMixin, UserIsOwnerMixin, DetailView):
    model = Scene
    pk_url_kwarg = 'scene_id'
    template_name = 'scenes/detail.html'


class CreateScene(LoginRequiredMixin, CreateView):
    model = Scene
    form_class = SceneForm
    pk_url_kwarg = 'scene_id'
    template_name = 'scenes/create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('scenes:detail', kwargs={'scene_id': self.object.id})


class EditScene(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Scene
    form_class = SceneForm
    pk_url_kwarg = 'scene_id'
    template_name = 'scenes/edit.html'

    def get_success_url(self):
        return reverse_lazy('scenes:detail', kwargs=self.kwargs)


class DeleteScene(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Scene
    pk_url_kwarg = 'scene_id'
    template_name = 'scenes/delete.html'
    success_url = reverse_lazy('scenes:index')
