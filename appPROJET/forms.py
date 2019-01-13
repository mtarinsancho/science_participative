from django import forms

class NewSpeciesForm(forms.Form):
	Nom_latin = forms.CharField(label='Nom latin', max_length=100)
	Nom_vern = forms.CharField(label='Nom vern', max_length=100)
	Date = forms.DateField(label='Date')
	Observateur = forms.CharField(label='Observateur', max_length=100)
	Localisation = forms.CharField(label='Localisation', max_length=100)
	Ecosystem = forms.CharField(label='Ecosystem', max_length=100)