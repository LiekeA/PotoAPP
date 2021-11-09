from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfilForm, EmploiForm, BlogForm
from .models import Profil, Equipe, Match, Adversaire, Emploi, Blog
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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

@login_required
def viewprofileprivate(request):
    """ profil = get_object_or_404(Profil, user_id = request.user) """
    try:
        profil = Profil.objects.get(user_id=request.user)
        print(profil.id)
        identif = profil.id 
        emploi = Emploi.objects.get(profil_id = identif)
        profil.poste = profil.get_poste_display()
        return render(request, 'club/viewprofil.html', {'profil': profil, 'emploi':emploi})
    except Profil.DoesNotExist:
        return redirect('club:createprofile')
    except Emploi.DoesNotExist:
        return render(request, 'club/viewprofil.html', {'profil': profil})


def viewequipe(request, equipe):
    equipe = get_object_or_404(Equipe, id = equipe )
    joueurs = Profil.objects.filter(equipe_id = equipe).select_related('user')
    return render(request, 'club/viewequipe.html', {'equipe': equipe , 'joueurs':joueurs })

@login_required
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

@login_required
def deleteprofil(request):
    profil = get_object_or_404(Profil, user_id=request.user)
    if request.method == 'POST':
        profil.delete()
        return redirect('home')

#match
def viewmatch(request, team):
    equipe = get_object_or_404(Equipe, id = team )
    now = timezone.now()
    lasts = Match.objects.filter(date__lt=now, equipe_id=team).order_by('-date').select_related('equipe', 'adversaire')
    upcomings = Match.objects.filter(date__gte=now, equipe_id=team).order_by('date').select_related('equipe', 'adversaire')


    matchs = Match.objects.filter(equipe_id=team)
    allteams = Adversaire.objects.filter(equipe_id = team, saison = 1).values_list("points","nom").union(Equipe.objects.filter(id = team).values_list("points","equipe")).order_by('-points')

    return render(request, 'club/viewmatch.html', {'equipe': equipe ,'matchs': matchs , 'allteams': allteams , 'lasts':lasts, 'upcomings':upcomings})


#classement

def viewclassement(request, team):
        equipe = get_object_or_404(Equipe, id = team )
        allteams = Adversaire.objects.filter(equipe_id = team, saison = 1).values_list("points","nom").union(Equipe.objects.filter(id = team).values_list("points","equipe")).order_by('-points')
        return render(request, 'club/viewclassement.html', {'equipe': equipe ,'allteams': allteams })


#reseau pro
@login_required
def createemploi(request):
    if request.method == 'GET':
        return render(request, 'club/createemploi.html', {'form':EmploiForm()})
    else:
        try:
            profil = get_object_or_404(Profil, user_id=request.user)
            form = EmploiForm(request.POST, request.FILES or None) 
            print(request.FILES)
            newemploi = form.save(commit=False)
            newemploi.profil_id = profil.id
            newemploi.save()
            return redirect('home')
        except IntegrityError :
            return render(request, 'club/createemploi.html', {'form': EmploiForm(),'error': 'Vous avez déja un profil'})


def viewemploi(request):
    if request.method == 'GET':
        emplois = Emploi.objects.all().order_by('-id')
        return render(request, 'club/viewemploi.html', {'emplois': emplois})


#Blog
@login_required
def createblog(request):
    if request.method == 'GET':
        return render(request, 'club/createblog.html', {'form':BlogForm()})
    else:
        profil = get_object_or_404(Profil, user_id=request.user)
        form = BlogForm(request.POST, request.FILES or None) 
        print(request.FILES)
        newblog = form.save(commit=False)
        newblog.auteur_id = profil.id
        newblog.save()
        return redirect('home')

def viewblogs(request):
    blogs = Blog.objects.order_by('-date')
    return render(request, 'club/allblogs.html', {'blogs' : blogs})

def detailblog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'club/detailblog.html', {'blog':blog})


#paiement de la licence_is_paid

def licencePayment(request):
    if request.method == 'GET':
        return render(request, 'club/licencePayment.html')    