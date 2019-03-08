from django.db import models

from user_manager.models import User


# TODO This model will change in the future. All fields, especially place, characters, rewards and encounters
# TODO are due to change to more complex classes
class Scene(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField("Name", max_length=200, null=False, default="Fabulous Scene")
    description = models.TextField("Description", max_length=20000, null=True, blank=True)
    place = models.CharField("Place", max_length=200, null=True, blank=True)
    characters = models.TextField("Characters", max_length=20000, null=True, blank=True)
    rewards = models.TextField("Rewards", max_length=20000, null=True, blank=True)
    encounters = models.TextField("Encounters", max_length=20000, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
