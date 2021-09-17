from django.contrib import admin


# Register your models here.
from .models import Profil, Emploi, Famille, Equipe, Match
# Register your models here.
#Ajoute la catégorie Project a la bdd dans la page /admin/
admin.site.register(Profil)
admin.site.register(Emploi)
admin.site.register(Famille)
admin.site.register(Equipe)
admin.site.register(Match)