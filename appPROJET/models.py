from django.db import models


class Specie(models.Model):
    Nom_latin = models.TextField(null=True)
    Nom_vern = models.TextField(null=True)


class Ecosystem(models.Model):
    Name = models.TextField(null=True)

    species = models.ManyToManyField(Specie, related_name='ecosystems', blank=True)
