from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def about2(request):
    return render(request, 'main/about2.html')

def contacts_view(request):
    return render(request, 'main/contacts.html')