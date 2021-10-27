from django.contrib import admin


# Register your models here.
from .models import Profil, Emploi, Famille, Equipe, Match, Adversaire, Saison, Blog
# Register your models here.
#Ajoute la catégorie Project a la bdd dans la page /admin/
admin.site.register(Profil)
admin.site.register(Emploi)
admin.site.register(Famille)
admin.site.register(Equipe)
admin.site.register(Match)
admin.site.register(Adversaire)
admin.site.register(Saison)
admin.site.register(Blog)