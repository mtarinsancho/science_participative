from django.db import models

class table1 (models.Model):
	Nom_latin = models.TextField(null=True)
	Nom_vern = models.TextField(null=True)


