from django.db import models

from user_manager.models import User


class PlaylistItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField("Name", max_length=100, null=False, default="Ambience Music")
    # To which service does the playlist belong? (Default is Spotify, but can be more in future)
    service = models.CharField("Service", max_length=100, null=False, default="Spotify")
    # We do not use Djangos URL field because in the future we might need more complex content
    uri = models.CharField("URI", max_length=1000, null=False,
                           default="https://open.spotify.com/user/cate.falconer/playlist/7dFPewHpqOdEb3E88AZhYC?si=sFYcXn4SRSOF2sHYoFQ1Yg")

    @property
    def play_link(self):
        if self.service.lower() == "spotify":
            return self.uri
        return self.uri

    def __str__(self):
        return self.name


# TODO This model will change in the future. All fields, especially place, characters, rewards and encounters
# TODO are due to change to more complex classes
class Scene(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField("Name", max_length=200, null=False, default="Faboulous Scene")
    description = models.TextField("Description", max_length=20000, null=True, blank=True)
    place = models.CharField("Place", max_length=200, null=True, blank=True)
    characters = models.TextField("Characters", max_length=20000, null=True, blank=True)
    rewards = models.TextField("Rewards", max_length=20000, null=True, blank=True)
    encounters = models.TextField("Encounters", max_length=20000, null=True, blank=True)
    sound_effects = models.ForeignKey(PlaylistItem, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)

    def __str__(self):
        return self.name
