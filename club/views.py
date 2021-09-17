from django.shortcuts import render, redirect
from .forms import ProfilForm
from .models import Profil
from django.db import IntegrityError

# Create your views here.

def createprofile(request):
    if request.method == 'GET':
        return render(request, 'club/test.html', {'form':ProfilForm()})
    else:
        form = ProfilForm(request.POST)
        try:
            newprofile = form.save(commit=False)
            newprofile.user = request.user
            print(newprofile.user)
            newprofile.save()
            return redirect('home')
        except IntegrityError :
            return render(request, 'club/test.html', {'form': ProfilForm(),'error': 'Vous avez déja un profil'})
        """ except ValueError :
            return render(request, 'club/test.html', {'form': ProfilForm(),'error': 'saisie incorrecte'})
 """
