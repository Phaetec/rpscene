from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    is_premium = models.BooleanField(null=False, default=False)
    username = models.CharField(null=False, unique=True, max_length=50)
    email = models.EmailField(null=False, unique=True, max_length=200)

    def __str__(self):
        return self.username
