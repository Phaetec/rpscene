from django.db import models


# TODO This model will change in the future. All fields, especially place, characters, rewards and encounters
# TODO are due to change to more complex classes
class Scene(models.Model):
    name = models.CharField("Name", max_length=200, null=False, default="Faboulous Scene")
    description = models.TextField("Description", max_length=20000, null=True, blank=True)
    place = models.CharField("Place", max_length=200, null=True, blank=True)
    characters = models.TextField("Characters", max_length=20000, null=True, blank=True)
    rewards = models.TextField("Rewards", max_length=20000, null=True, blank=True)
    encounters = models.TextField("Encounters", max_length=20000, null=True, blank=True)

    def __str__(self):
        return self.name
