from django.contrib import admin


# Register your models here.
from .models import Partenaire
# Register your models here.
#Ajoute la catégorie Project a la bdd dans la page /admin/
admin.site.register(Partenaire)
