from django.urls import path
from club import views

app_name = 'club'

urlpatterns = [
    path('creation-profil', views.createprofile, name='createprofile'),
]

