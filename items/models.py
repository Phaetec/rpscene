from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField("Name", max_length=200, null=False, default="")
    weight = models.FloatField("Weight (pounds)", null=False)
    type = models.CharField("Type", max_length=200, null=False, default="Unknown")
    description = models.TextField("Description", max_length=10000, null=False, default="")
