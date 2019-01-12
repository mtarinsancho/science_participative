from django import forms

class NewSpeciesForm(forms.Form):
	Nom_latin = forms.CharField(label='Nom latin', max_length=100)
	Nom_vern  = forms.CharField(label='Nom vern', max_length=100)