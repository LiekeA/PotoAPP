from django.urls import path
from club import views
from django.conf import settings
"""from django.conf.urls.static import static"""


app_name = 'club'

urlpatterns = [
    path('creation-profil', views.createprofile, name='createprofile'),
    path('profil/', views.viewprofileprivate, name='viewprofileprivate'),
    path('equipe/<int:equipe>', views.viewequipe, name='viewequipe'),
    path('modifier-profil/', views.updateprofil, name='updateprofil'),
    path('supprimer-profil/', views.deleteprofil, name='deleteprofil'),

    #match
    path('match/equipe-<int:team>', views.viewmatch, name='viewmatch'),

    #réseau pro
    path('reseau-pro/creation', views.createemploi, name='createemploi'),
    path('reseau-pro/tout-le-reseau', views.viewemploi, name='viewemploi'),

    #blog
    path('blog/creation', views.createblog, name='createblog'),
    path('blog/', views.viewblogs, name='viewblogs'),
    path('blog/<int:blog_id>/', views.detailblog, name='detailblog'),
    
    #paiement de la licence
    path('licence/', views.licencePayment, name='licencePayment'),
]

"""if settings.DEBUG:"""
"""urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""