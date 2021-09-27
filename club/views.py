from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfilForm
from .models import Profil, Equipe
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def createprofile(request):
    if request.method == 'GET':
        return render(request, 'club/createprofil.html', {'form':ProfilForm()})
    else:
        form = ProfilForm(request.POST, request.FILES or None) 
        print(request.FILES)
        try:
            newprofile = form.save(commit=False)
            newprofile.user = request.user
            print(newprofile.user)
            newprofile.save()
            return redirect('home')
        except IntegrityError :
            return render(request, 'club/createprofil.html', {'form': ProfilForm(),'error': 'Vous avez déja un profil'})
        """ except ValueError :
            return render(request, 'club/createprofil.html', {'form': ProfilForm(),'error': 'saisie incorrecte'})
 """

def viewprofileprivate(request):
    """ profil = get_object_or_404(Profil, user_id = request.user) """
    try:
        profil = Profil.objects.get(user_id=request.user)
        print(profil.num_maillot)
        profil.poste = profil.get_poste_display()
        return render(request, 'club/viewprofil.html', {'profil': profil})
    except Profil.DoesNotExist:
        return redirect('club:createprofile')

def viewequipe(request, equipe):
    equipe = get_object_or_404(Equipe, id = equipe )
    joueurs = Profil.objects.filter(equipe_id = equipe).select_related('user')
    print(joueurs.query) 
    return render(request, 'club/viewequipe.html', {'equipe': equipe , 'joueurs':joueurs })

def updateprofil(request):
    profil = get_object_or_404(Profil, user_id=request.user)
    if request.method == 'GET':
        form = ProfilForm(instance=profil)
        return render(request, 'club/updateprofil.html', {'profil': profil, 'form':form})
    else:
        try:
            form = ProfilForm(request.POST, request.FILES, instance=profil)
            print(request.FILES)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'club/updateprofil.html' , {'profil':profil, 'form':form, 'error':'erreur'} )

def deleteprofil(request):
    profil = get_object_or_404(Profil, user_id=request.user)
    if request.method == 'POST':
        profil.delete()
        return redirect('home')