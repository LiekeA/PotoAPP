from django.db import models

# Create your models here.
class Compte(models.Model):

    nom = models.CharField(max_length = 30, default="")    
    montant = models.DecimalField(max_digits=19, decimal_places=2)
    montant_initial = models.DecimalField(max_digits=19, decimal_places=2,default='0')
    def __str__(self):
        return self.nom    

class Transaction(models.Model):

    TYPE = (
                    ('entree', 'Entrée'),
                    ('depense', 'Dépense'),
                    )

    CATEGORIES = (
                        ('licence', 'Licence'),
                        ('Sponsor', 'Sponsor'),
                        ('Don', 'Don'),
                        ('Materiel', 'Matériel'),
                        ('Arbitre', 'Arbitre'),
                        ('Assurances', 'Assurances'),
                        ('Collation', 'Collation'),
                        ('Remboursement', 'Remboursement'),
                        )

    account = models.ForeignKey(Compte, on_delete=models.CASCADE)
    type_trans = models.CharField(max_length = 10, choices = TYPE, verbose_name = "Type de transaction")
    categorie = models.CharField(max_length = 20, choices = CATEGORIES)
    description = models.CharField(max_length = 200)
    montant = models.DecimalField(max_digits=19, decimal_places=2)
    remboursement = models.CharField(max_length = 30, verbose_name = "Personne à rembourser", default="")
    
    def __str__(self):
        return self.description

    def save(self):
       self.account.montant += self.montant
       self.account.save()
       super(Transaction, self).save() # Call the real save() method

    def delete(self):
       self.account.montant -= self.montant
       self.account.save()
       super(Transaction, self).delete()