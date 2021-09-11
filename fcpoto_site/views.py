from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django import forms
from fcpoto_site.forms import RegisterForm
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'fcpoto/home.html')

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
        
        """ form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save() 
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.first_name = form.cleaned_data.get('first_name')
                user.last_name = form.cleaned_data.get('last_name')
                user.email = form.cleaned_data.get('email')
                user.save()
                login(request, user)
                messages.success(request, "Registration successful." )
                return redirect('home')
            except IntegrityError:
                return render(request, 'fcpoto/signupuser.html', {'form': RegisterForm(), 'error': 'Ce pseudo est déjà pris'})
        else:
            form = RegisterForm(request.POST)
            return render (request, 'fcpoto/signupuser.html', {"form":form})  
            return render(request, 'fcpoto/signupuser.html', {'form': RegisterForm(), 'error': form.errors})    """


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

def profile(request):
    if request.method == 'GET':
        return render(request, 'fcpoto/profile.html')