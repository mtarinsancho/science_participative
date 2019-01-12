from django.db.models import Q
from django.shortcuts import render
from appPROJET.models import Specie, Ecosystem
from .forms import NewSpeciesForm
from django.views.decorators.csrf import csrf_exempt

def species_in_ecosystem(request, ecosystem_name):5
    # /ecosystem/get/forest
    # Get the specific ecosystem via 'ecosystem_name'
    my_ecosystem = Ecosystem.objects.get(Name=ecosystem_name)
    # Find all the species associated with the SPECIFIC ecosystem (e.g., 'forest' -> loup, orchis mâle)
    species_in_ecosystem = my_ecosystem.species.all()
    return render(request, "templates/speciesecosystem.html", {"species_in_ecosystem": species_in_ecosystem})


def affichetable(request):
    """Show all the entries in the database"""
    all_species_in_table = Specie.objects.all()
    return render(request, "templates/appelfiches.html", {"species_table": all_species_in_table})


def show_especes(request, search_text):
    # Lookup for species that contain the given text in 'Nom_latin' field or (|) in 'Nom_vern' field
    species = Specie.objects.filter(Q(Nom_latin=search_text) | Q(Nom_vern=search_text))
    return render(request, "templates/sp.html", {"species": species})


@csrf_exempt
def new_species_form(request):
    # /createNewSpecies?Nom_latin=Buho&Nom_vern=Pardo
    # <QueryDict: {'Nom_latin': ['Buho'], 'Nom_vern': ['Pardo']}>
    nom_latin = request.GET.get('Nom_latin')
    nom_vern = request.GET.get('Nom_vern')

    # If the variables are created (are in the URL) then create the species entry in the database
    if nom_latin and nom_vern:

        specie = Specie(
            Nom_latin=nom_latin,
            Nom_vern=nom_vern
        )
        specie.save()
        # return redirect('/newSpecies')
        return render(request, 'success_add_species.html')

    # If not come back to the original form
    else:
        form = NewSpeciesForm()

    return render(request, 'especes.html', {'form': form})
