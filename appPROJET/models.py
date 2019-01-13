from django.db import models


class Specie(models.Model):
    Nom_latin = models.TextField(null=True)
    Nom_vern = models.TextField(null=True)
    Date = models.DateTimeField(auto_now_add=True, auto_now=False)
    Observateur = models.TextField(null=True)


class Ecosystem(models.Model):
    Name = models.TextField(null=True)
#Link between the table species and the table ecosystems. related_name -> foreign key.
    species = models.ManyToManyField(Specie, related_name='ecosystem', blank=True)
