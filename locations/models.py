from django.db import models

from user_manager.models import User


class Location(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    name = models.CharField("Name", max_length=200, null=False, default="A wonderful place")
    description = models.TextField("Description", max_length=20000, null=True, blank=True)

    def __str__(self):
        return self.name
