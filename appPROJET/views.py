from django.db.models import Q
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from appPROJET.models import Specie, Ecosystem, Sheets
from .forms import NewSpeciesForm


# Show all observations in the database
def affichetable(request):
    """Show all the entries in the database"""
    all_species_in_table = Specie.objects.all()
    return render(request, "templates/appelfiches.html", {"species_table": all_species_in_table})


# Lookup for species that contain the given text in 'Nom_latin' field or (|) in 'Nom_vern' field
def show_especes(request, search_text):
    species = Specie.objects.filter(Q(Nom_latin=search_text) | Q(Nom_vern=search_text))
    print(species)
    return render(request, "templates/sp.html", {"species": species})


# Lookup for all species in a specific ecosystem
def species_in_ecosystem(request, ecosystem_name):
    # /ecosystem/get/forest
    # Get the specific ecosystem via 'ecosystem_name'
    my_ecosystem = Ecosystem.objects.get(Name=ecosystem_name)
    # Find all the species associated with the SPECIFIC ecosystem (e.g., 'forest' -> loup, orchis mâle)
    species_in_ecosystem = my_ecosystem.species.all()
    return render(request, "templates/speciesecosystem.html", {"species_in_ecosystem": species_in_ecosystem})


# Save a new species observation:
@csrf_exempt
def new_species_form(request):
    # /createNewSpecies?Nom_latin=Buho&Nom_vern=Pardo&Date=19/07/2018&Observateur=Maria
    # <QueryDict: {'Nom_latin': ['Buho'], 'Nom_vern': ['Pardo']}>
    nom_latin = request.GET.get('Nom_latin')
    nom_vern = request.GET.get('Nom_vern')
    date = request.GET.get('Date')
    observateur = request.GET.get('Observateur')
    localisation = request.GET.get('Localisation')
    ecosystem_name = request.GET.get('Ecosystem')

    # If the variables are created (are in the URL) then create the species entry in the database
    # 'if' checks if the variables are not empty.
    if nom_latin and nom_vern and date and observateur and ecosystem_name:

        # As ecosystem is a foreign key in the specie table, we need to use get or create which gives two variables : the new or not new (True or False) and the object
        # As it gives you two solutions, we need two variables ecosystem (the entry of the ecosystem name) and created(True or false)
        # By default

        ecosystem, created = Ecosystem.objects.get_or_create(Name=ecosystem_name)

        specie = Specie(
            Nom_latin=nom_latin,
            Nom_vern=nom_vern,
            Date=date,
            Observateur=observateur,
        )
        specie.save()

        # To add the object ecosystem (the entry from the html) as a foreign key of the specie(entry) that you just created and that will be saved in the table "Specie".
        # (Link two tables with a Many to Many relations)

        specie.ecosystems.add(ecosystem)

        # return redirect('/newSpecies')
        return render(request, 'success_add_species.html')

    # If not come back to the original form
    else:
        form = NewSpeciesForm()

    return render(request, 'especes.html', {'form': form})


# Show all species sheets
def show_sheets(request):
    all_sheets_in_table = Sheets.objects.all()
    return render(request, "templates/showsheets.html", {"sheets": all_sheets_in_table})


# Search one species sheet by both latin and vernacular name
def sheet_search(request, search_text):
    sheets = Sheets.objects.filter(Q(Nom_latin=search_text) | Q(Nom_vern=search_text))
    return render(request, "templates/sheetsearch.html", {"sheets": sheets})
