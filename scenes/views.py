from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from scenes.forms import SceneForm, PlaylistItemForm
from scenes.models import Scene, PlaylistItem


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


# Playlist Scenes

class PlayListIndexScene(LoginRequiredMixin, ListView):
    model = PlaylistItem
    template_name = 'scenes/playlists/index.html'
    context_object_name = 'playlists'
    paginate_by = 10

    def get_queryset(self):
        return PlaylistItem.objects.filter(owner=self.request.user)


class PlayListDetailScene(LoginRequiredMixin, UserIsOwnerMixin, DetailView):
    model = PlaylistItem
    context_object_name = 'playlist'
    pk_url_kwarg = 'playlistitem_id'
    template_name = 'scenes/playlists/detail.html'


class PlayListCreateScene(LoginRequiredMixin, CreateView):
    model = Scene
    form_class = PlaylistItemForm
    pk_url_kwarg = 'playlistitem_id'
    template_name = 'scenes/playlists/create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('scenes:playlist.detail', kwargs={'playlistitem_id': self.object.id})


class PlayListEditScene(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = PlaylistItem
    form_class = PlaylistItemForm
    pk_url_kwarg = 'playlistitem_id'
    template_name = 'scenes/playlists/edit.html'

    def get_success_url(self):
        return reverse_lazy('scenes:playlist.detail', kwargs=self.kwargs)


class PlayListDeleteScene(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = PlaylistItem
    pk_url_kwarg = 'playlistitem_id'
    template_name = 'scenes/playlists/delete.html'
    success_url = reverse_lazy('scenes:playlist.index')
