"""PROJET URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from appPROJET.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
	url(r'appelfiches$', affichetable, name='species_table'),
    path('sp/get/<search_text>', show_especes, name='especes'),
    url(r'createNewSpecies$', new_species_form),
    path('speciesecosystem/get/<ecosystem_name>', species_in_ecosystem, name='species_in_ecosystem' ),
    url(r'showsheets$', show_sheets, name='fiches_especes')
]

