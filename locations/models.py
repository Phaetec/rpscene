import uuid
from django.db import models

from user_manager.models import User


def map_filepath(instance, filename: str) -> str:
    random_uuid = uuid.uuid4()
    return 'user_{0}/{1}/{2}'.format(instance.owner.id, random_uuid, filename)


class RaceDistribution(models.Model):
    # This needs no owner, since it is always tied to a location
    location = models.ForeignKey("Location", on_delete=models.CASCADE, null=False)
    race = models.CharField("Race", max_length=100, null=False)
    percentage = models.FloatField("Percentage", null=False)

    def __str__(self):
        return "{} - {}".format(self.race, self.percentage)


class Location(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField("Name", max_length=200, null=False, default="A wonderful place")
    description = models.TextField("Description", max_length=20000, null=True, blank=True)
    type = models.CharField("Type", max_length=100, null=True, blank=True)
    # TODO ruler should probably change to character-foreign-key once its implemented
    ruler = models.CharField("Ruler / Owner", max_length=100, null=True, blank=True)
    history = models.TextField("History", max_length=20000, null=True, blank=True)
    map = models.ImageField("Map", null=True, blank=True, upload_to=map_filepath)

    def __str__(self):
        return self.name
