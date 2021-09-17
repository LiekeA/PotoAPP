from django.forms import ModelForm
from .models import Profil, Emploi, Famille, Equipe, Match
from django import forms
from django.conf import settings
class ProfilForm(ModelForm):
    date_naissance = forms.DateField(
    localize=True,
    widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
)
    class Meta:
        model = Profil
        fields = ['statut', 'num_maillot', 'poste','tel', 'date_naissance', 'adresse', 'cp', 'ville', 'num_licence', 'licence_is_paid', 'certif_medical', 'reglement']


class EmploiForm(ModelForm):
    class Meta:
        model = Emploi
        fields = ['titre', 'description','entreprise','entreprise_is_sponsor']


class FamilleForm(ModelForm):
    class Meta:
        model = Famille
        fields = ['prenom','date_naissance','lien']

class EquipeForm(ModelForm):
    class Meta:
        model = Equipe
        fields = ['equipe']

class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = ['journee','date','heure','lieu','adversaire','domicile','enjeu']