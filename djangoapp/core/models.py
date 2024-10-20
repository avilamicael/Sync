from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_client = models.BooleanField(default=True, verbose_name="É Cliente")
    is_professional = models.BooleanField(default=False, verbose_name="É Profissional")

    def __str__(self):
        return self.username
