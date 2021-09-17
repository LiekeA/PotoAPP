from django.db import models
from django.contrib.auth.models import User

class Equipe(models.Model):
    EQUIPE =(
        ('11', 'Équipe à 11'),
        ('7A', 'Équipe à 7 A'),
        ('7B', 'Équipe à 7 B'),
    )
    equipe = models.CharField(max_length=30, choices=EQUIPE)

class Profil(models.Model):
    CHOIX =(
        ('joueur', 'Joueur'),
        ('dirigeant', 'Dirigeant'),
    ) 
    POSTES =(
        ('gardien', 'Gardien'),
        ('def', 'Défenseur'),
        ('lat', 'Latéral'),
        ('mdef', 'Milieu Défensif'),
        ('moff', 'Milieu offensif'),
        ('ailier', 'Ailier'),
        ('attaquant', 'Attaquant'),
        ('arbitre', 'Arbitre'),
    ) 
    statut = models.CharField(max_length=30, choices= CHOIX)
    poste = models.CharField(max_length=50, choices= POSTES)
    num_maillot = models.SmallIntegerField()
    tel = models.IntegerField()
    date_naissance = models.DateField(null=True)
    adresse = models.CharField(max_length=50)
    cp = models.IntegerField()
    ville = models.CharField(max_length=50)
    num_licence = models.IntegerField()
    licence_is_paid = models.BooleanField(default=False)
    certif_medical = models.BooleanField(default=False)
    reglement = models.BooleanField(default=False)
    #foreignKey
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=True)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, null=True)

class Emploi(models.Model):
    titre = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    entreprise = models.CharField(max_length=30)
    entreprise_is_sponsor = models.BooleanField(default=False)
    profil = models.OneToOneField(Profil, on_delete=models.CASCADE)
    
class Famille(models.Model):
    LIEN =(
        ('joueur', 'Joueur'),
        ('dirigeant', 'Dirigeant'),
    ) 
    prenom = models.CharField(max_length = 30)
    date_naissance =  models.DateField(null=True)
    lien = models.CharField(max_length=30, choices= LIEN) 
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)



class Match(models.Model):
    ENJEU =(
        ('championnat', 'Championnat'),
        ('coupe', 'Coupe'),
    )
    equipe = models.ForeignKey(Equipe , on_delete=models.CASCADE)
    journee = models.IntegerField()
    date = models.DateField(null=True)
    heure = models.TimeField()
    lieu = models.CharField(max_length=60)
    adversaire = models.CharField(max_length=40)
    domicile = models.BooleanField(default=False)
    enjeu = models.CharField(max_length=30, choices=ENJEU, default='championnat')

