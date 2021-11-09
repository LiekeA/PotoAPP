from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django import forms
from fcpoto_site.forms import RegisterForm
from django.contrib import messages
from club.models import Match, Emploi, Profil, Blog
from fcpoto_site.models import Partenaire
from django.utils import timezone
from datetime import timedelta, datetime, date
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    now = timezone.now()
    
    #dernier match et match suivants des 3 équipes
    last11 = Match.objects.filter(date__lt=now, equipe_id=1).order_by('-date')[:1].select_related('equipe', 'adversaire')
    upcomings11 = Match.objects.filter(date__gte=now, equipe_id=1).order_by('date')[:1].select_related('equipe', 'adversaire')

    last7a = Match.objects.filter(date__lt=now, equipe_id=2).order_by('-date')[:1].select_related('equipe', 'adversaire')
    upcomings7a = Match.objects.filter(date__gte=now, equipe_id=2).order_by('date')[:1].select_related('equipe', 'adversaire')
    
    last7b = Match.objects.filter(date__lt=now, equipe_id=3).order_by('-date')[:1].select_related('equipe', 'adversaire')
    upcomings7b = Match.objects.filter(date__gte=now, equipe_id=3).order_by('date')[:1].select_related('equipe', 'adversaire')

    #3 derniers blog reseau pro
    emploi = Emploi.objects.all().order_by('-id')[:4].select_related('profil')
   
    
    #entreprise partenaires
    partenaires = Partenaire.objects.all()

    #anniversaires
    now_day, now_month = now.day, now.month
    today_anniv = Profil.objects.filter(date_naissance__day=now_day, date_naissance__month=now_month)

    month_anniv = Profil.objects.filter(date_naissance__month=now_month)
    print(month_anniv.query)

    #blog
    blogs = Blog.objects.all().order_by('-date')[:6]

   

    return render(request, 'fcpoto/home.html', {'upcomings7a':upcomings7a , 'last7a':last7a, 'upcomings7b':upcomings7b , 'last7b':last7b,'upcomings11':upcomings11 , 'last11':last11, 'emploi':emploi, 'partenaires':partenaires, 'today_anniv':today_anniv,'month_anniv':month_anniv, 'blogs':blogs})

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'fcpoto/signupuser.html' , {'form': RegisterForm()})
        print(form.errors.as_data())
    else:
        form = RegisterForm(request.POST)
        print(form.errors.as_json())
        form.errors.as_data()
        if form.is_valid():
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = form.save()
                    return redirect('home')
                except IntegrityError:
                    return render(request, 'fcpoto/signupuser.html', {'form': RegisterForm(), 'error': 'Ce pseudo est déjà pris'})
            else: 
                    return render(request, 'fcpoto/signupuser.html', {'form': RegisterForm(), 'error': 'Les mots de passe ne correspondent pas'})
        else:
            return render(request, 'fcpoto/signupuser.html', {'form': RegisterForm(), 'error': form.errors})
        
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'fcpoto/loginuser.html', {'form': AuthenticationForm()})
    else:
        """ form = UserCreationForm(request.POST['username']) """
        form = RegisterForm(request.POST['username'])
        print(form['username'].label_tag())
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'fcpoto/loginuser.html', {'form': AuthenticationForm(), 'error':"Le pseudo ou le mot de passe n'existe pas"})
        # Return an 'invalid login' error message.

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'fcpoto/change_password.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'GET':
        return render(request, 'fcpoto/profile.html')

def cgv(request):
    if request.method == 'GET':
        return render(request, 'fcpoto/cgv.html')

def legal(request):
    if request.method == 'GET':
        return render(request, 'fcpoto/legal.html')