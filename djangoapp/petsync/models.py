from django.db import models
from django.conf import settings

class Pet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Dono")
    name = models.CharField(max_length=100, verbose_name="Nome")
    species = models.CharField(max_length=50, verbose_name="Espécie")
    breed = models.CharField(max_length=100, blank=True, null=True, verbose_name="Raça")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Peso")
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Altura")
    photo = models.ImageField(upload_to='pet_photos/', blank=True, null=True, verbose_name="Foto")
    vaccinations = models.TextField(blank=True, null=True, verbose_name="Vacinações")

    def __str__(self):
        return self.name
