from django.db.models import Q
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from appPROJET.models import Specie
from .forms import NewSpeciesForm


def affichetable(request):
    """Show all the entries in the database"""
    all_species_in_table = Specie.objects.all()
    return render(request, "templates/appelfiches.html", {"species_table": all_species_in_table})


def showEspeces(request, search_text):
    # Lookup for species that contain the given text in 'Nom_latin' field or (|) in 'Nom_vern' field
    species = Specie.objects.filter(Q(Nom_latin=search_text) | Q(Nom_vern=search_text))

    return render(request, "templates/sp.html", {"species": species})


@csrf_exempt
def newSpeciesForm(request):
    # /createNewSpecies?Nom_latin=Buho&Nom_vern=Pardo
    # <QueryDict: {'Nom_latin': ['Buho'], 'Nom_vern': ['Pardo']}>

    nom_latin = request.GET.get('Nom_latin')
    nom_vern = request.GET.get('Nom_vern')

    # Check that the fields are in the URL
    if nom_latin and nom_vern:

        specie = Specie(
            Nom_latin=nom_latin,
            Nom_vern=nom_vern
        )
        specie.save()
        # return redirect('/newSpecies')
        return render(request, 'success_add_species.html')

    else:
        form = NewSpeciesForm()

    return render(request, 'especes.html', {'form': form})
