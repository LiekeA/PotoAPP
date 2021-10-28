from django.forms import ModelForm
from .models import Profil , Emploi, Famille, Equipe, Match, Adversaire, Blog
from django import forms
from django.conf import settings

class ProfilForm(ModelForm):
    date_naissance = forms.DateField(
    localize=True,
    widget=forms.DateInput(format = '%Y-%m-%d',attrs={'type': 'date'}),
)
    anciennete = forms.DateField(
    localize=True,
    widget=forms.DateInput(format = '%Y-%m',attrs={'type': 'date'}),
)
    photo_face = forms.ImageField()
    photo_dos = forms.ImageField()
    class Meta:
        model = Profil
        fields = ['statut', 'num_maillot', 'poste', 'anciennete', 'tel', 'date_naissance', 'adresse', 'cp', 'ville', 'num_licence', 'certif_medical', 'reglement', 'equipe', 'photo_face','photo_dos']
    

class EmploiForm(ModelForm):
    class Meta:
        model = Emploi
        fields = ['titre', 'description','entreprise','entreprise_is_sponsor', 'logo_entreprise']


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
        fields = ['journee','date','heure','lieu','adversaire','domicile','enjeu','saison']

class AdversaireForm(ModelForm):
    class Meta:
        model = Adversaire
        fields = ['nom','points','equipe','saison']

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['theme','titre','contenu','photo']