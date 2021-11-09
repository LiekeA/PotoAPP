from django.db import models
from django.contrib.auth.models import User

class Equipe(models.Model):
    EQUIPE =(
        ('11', 'Équipe à 11'),
        ('7A', 'Équipe à 7 A'),
        ('7B', 'Équipe à 7 B'),
        ('ancien', 'Les anciens membres'),
    )
    equipe = models.CharField(max_length=30, choices=EQUIPE)
    points = models.IntegerField(default='0')
    logo = models.ImageField(upload_to='club/images/',blank=True)
    def __str__(self):
        return self.equipe

class Profil(models.Model):
    CHOIX =(
        ('joueur', 'Joueur'),
        ('dirigeant', 'Dirigeant'),
        ('ancien', 'Ancien membre'),
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
        ('entraineur', 'Entraineur'),
    ) 
    statut = models.CharField(max_length=30, choices= CHOIX)
    poste = models.CharField(max_length=50, choices= POSTES)
    num_maillot = models.SmallIntegerField()
    anciennete = models.DateField(blank=True, null=True)
    tel = models.IntegerField()
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=50)
    cp = models.IntegerField()
    ville = models.CharField(max_length=50)
    num_licence = models.IntegerField()
    licence_is_paid = models.BooleanField(default=False)
    certif_medical = models.BooleanField(default=False)
    reglement = models.BooleanField(default=False)
    #foreignKey
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE, default='1')
    photo_face = models.ImageField(upload_to='club/images/', blank=True)
    photo_dos = models.ImageField(upload_to='club/images/',blank=True)
    
    def __str__(self):
        return self.user.username

class Emploi(models.Model):
    titre = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    entreprise = models.CharField(max_length=30)
    entreprise_is_sponsor = models.BooleanField(default=False)
    profil = models.OneToOneField(Profil, on_delete=models.CASCADE)
    logo_entreprise = models.ImageField(upload_to='club/images/',blank=True)
    
class Famille(models.Model):
    LIEN =(
        ('joueur', 'Joueur'),
        ('dirigeant', 'Dirigeant'),
    ) 
    prenom = models.CharField(max_length = 30)
    date_naissance =  models.DateField()
    lien = models.CharField(max_length=30, choices= LIEN) 
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, default='1')

class Saison(models.Model):
    saison = models.CharField(max_length=20)
    def __str__(self):
        return self.saison    

class Adversaire(models.Model):
    nom = models.CharField(max_length=30)
    points = models.IntegerField(default='0') 
    equipe = models.ForeignKey(Equipe , on_delete=models.CASCADE, default='1')
    saison = models.ForeignKey(Saison , on_delete=models.CASCADE, default='1')
    def __str__(self):
        return self.nom    


class Match(models.Model):
    ENJEU =(
        ('championnat', 'Championnat'),
        ('coupe', 'Coupe'),
        ('amical', 'Amical'),
    )
    equipe = models.ForeignKey(Equipe , on_delete=models.CASCADE, default='1')
    adversaire = models.ForeignKey(Adversaire , on_delete=models.CASCADE, default='1')
    saison = models.ForeignKey(Saison , on_delete=models.CASCADE,default='1')
    journee = models.IntegerField()
    date = models.DateField()
    heure = models.TimeField()
    lieu = models.CharField(max_length=60)
    domicile = models.BooleanField(default=False)
    score_fcpoto = models.IntegerField(default='0')
    score_adversaire = models.IntegerField(default='0')
    enjeu = models.CharField(max_length=30, choices=ENJEU, default='championnat')

    def __str__(self):
        return self.adversaire.nom
    

class Blog(models.Model):
    THEME=(
        ('vie_club', 'Vie du club'),
        ('evenement', 'Événement'),
        ('sortie', 'Sortie'),
    )
    theme = models.CharField(max_length = 30, choices=THEME, default='vie_club')
    titre = models.CharField(max_length= 40)
    contenu = models.TextField(max_length= 4000)
    auteur = models.ForeignKey(Profil, on_delete=models.CASCADE, default='1')
    photo = models.ImageField(upload_to='club/images/blog/',blank=True)
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.titre