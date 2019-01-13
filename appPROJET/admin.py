from django.contrib import admin

from appPROJET.models import Specie, Ecosystem, Sheets


@admin.register(Specie)
class SpeciesAdmin(admin.ModelAdmin):
    fields = ('Nom_latin', 'Nom_vern', 'Observateur')


class SpeciesAccessInline(admin.StackedInline):
    model = Ecosystem.species.through


@admin.register(Ecosystem)
class EcosystemAdmin(admin.ModelAdmin):
    fields = ('Name','species')
    inlines = [
        SpeciesAccessInline,
    ]

@admin.register(Sheets)
class SpeciesAdmin(admin.ModelAdmin):
    fields = ('Nom_latin', 'Nom_vern', 'Description', 'Status')

