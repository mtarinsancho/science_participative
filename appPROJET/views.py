from django.shortcuts import render
from appPROJET.models import table1
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from .forms import NewSpeciesForm


def affichetable(request):
	table = table1.objects.all()
	return render(request, "templates/appelfiches.html", { "table1" : table})





def showEspeces(request, nom_vern):
	especes = table1.objects.get(Nom_vern=nom_vern)
	return render(request, "templates/sp.html", {"especes" : especes})

@csrf_exempt
def newSpeciesForm(request):
	if request.method == 'POST':
		form = NewSpeciesForm(request.POST)
		if form.is_valid():
			species = table1(Nom_latin = form.cleaned_data['Nom_latin'],
							 Nom_vern  = form.cleaned_data['Nom_vern'])
			species.save()
			#return redirect('/newSpecies')
			return render(request, 'success_add_species.html')
	else:
		form = NewSpeciesForm()
	return render(request, 'especes.html', {'form' : form})
