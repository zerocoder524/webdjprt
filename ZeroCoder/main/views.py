from django.shortcuts import render
from datetime import datetime


def index(request):
    current_year = datetime.now().year  # Получаем текущий год
    return render(request, 'main/index.html', {'caption': "CatDjango", 'current_year': current_year})


def new(request):
    current_year = datetime.now().year
    return render(request, 'main/new.html', {'current_year': current_year})


def third(request):
    current_year = datetime.now().year
    return render(request, 'main/third.html', {'current_year': current_year})


def fourth(request):
    current_year = datetime.now().year
    return render(request, 'main/fourth.html', {'current_year': current_year})


def about(request):
    return render(request, 'main/about.html')