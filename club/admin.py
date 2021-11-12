from django.contrib import admin


# Register your models here.
from .models import Profil, Emploi, Famille, Equipe, Match, Adversaire, Saison, Blog
# Register your models here.
#Ajoute la catégorie Project a la bdd dans la page /admin/

class Profiladmin(admin.ModelAdmin):
    list_display = ('user','tel','licence_is_paid')

class Matchadmin(admin.ModelAdmin):
    list_display = ('equipe','adversaire','date', 'enjeu')
    list_filter = ('equipe', 'enjeu')



admin.site.register(Profil,Profiladmin)
admin.site.register(Emploi)
admin.site.register(Famille)
admin.site.register(Equipe)
admin.site.register(Match,Matchadmin)
admin.site.register(Adversaire)
admin.site.register(Saison)
admin.site.register(Blog)