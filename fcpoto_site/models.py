from django.db import models

# Create your models here.

class Partenaire(models.Model):
    entreprise = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    logo_entreprise = models.ImageField(upload_to='club/images/',blank=True)
    def __str__(self):
        return self.entreprise

