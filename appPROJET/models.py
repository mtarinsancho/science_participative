from django.db import models


class Specie(models.Model):
    Nom_latin = models.TextField(null=True)
    Nom_vern = models.TextField(null=True)
    Date = models.DateTimeField(auto_now_add=True, auto_now=False)
    Observateur = models.TextField(null=True)
    Localisation = models.TextField(null=True)

# Show the variable with a name instead of a identity number (primary key). Here we choose Nom_latin which represents a line in Specie.

    def __str__(self):
        return self.Nom_latin

class Ecosystem(models.Model):
    Name = models.TextField(null=True)
#Link between the table species and the table ecosystems. related_name -> foreign key.
    species = models.ManyToManyField(Specie, related_name='ecosystems', blank=True)

    def __str__(self):
        return self.Name


class Sheets(models.Model):
    Nom_latin = models.TextField(null=True)
    Nom_vern = models.TextField(null=True)
    Description = models.TextField(null=True)
    Status = models.TextField(null=True)



