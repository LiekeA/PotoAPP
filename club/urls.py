from django.urls import path
from club import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'club'

urlpatterns = [
    path('creation-profil', views.createprofile, name='createprofile'),
    path('profil/', views.viewprofileprivate, name='viewprofileprivate'),
    path('equipe/<int:equipe>', views.viewequipe, name='viewequipe'),
    path('modifier-profil/', views.updateprofil, name='updateprofil'),
    path('supprimer-profil/', views.deleteprofil, name='deleteprofil'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)