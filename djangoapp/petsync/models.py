from django.db import models
from django.conf import settings

class Pet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    breed = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    photo = models.ImageField(upload_to='pet_photos/', blank=True, null=True)
    vaccinations = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
