from django.db import models

# Create your models here.
from user_manager.models import User


class HuePair(models.Model):
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE, unique=True)
    hue_key = models.CharField(max_length=200, blank=True, null=False, default="")
