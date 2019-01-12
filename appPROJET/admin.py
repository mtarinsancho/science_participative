from django.contrib import admin

from appPROJET.models import Specie, Ecosystem


@admin.register(Specie)
class SpeciesAdmin(admin.ModelAdmin):
    fields = ('Nom_latin', 'Nom_vern',)


@admin.register(Ecosystem)
class EcosystemAdmin(admin.ModelAdmin):
    fields = ('Name',)
