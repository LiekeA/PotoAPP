from django.db import models

# Create your models here.


class Produit(models.Model):
    CATEGORIES=(
        ('vetement', 'Vêtement'),
        ('masque', 'Masque'),
    )
    categories = models.CharField(max_length = 30, choices=CATEGORIES, default='vetement')
    nom = models.CharField(max_length = 30)
    description = models.TextField(max_length=200)
    prix = models.IntegerField()
    photo = models.ImageField(upload_to='club/images/shop/',blank=True)
    url = models.URLField(max_length=150)
    def __str__(self):
        return self.nom
