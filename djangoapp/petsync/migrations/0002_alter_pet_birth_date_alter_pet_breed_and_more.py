# Generated by Django 5.1.2 on 2024-10-20 22:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsync', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='breed',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Raça'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Altura'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Dono'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pet_photos/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.CharField(max_length=50, verbose_name='Espécie'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='vaccinations',
            field=models.TextField(blank=True, null=True, verbose_name='Vacinações'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Peso'),
        ),
    ]
