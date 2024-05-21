from django.shortcuts import render
from main.models import Animais

def index(request):
    animais = Animais.objects.all()
    return render(request, 'main/index.html', {"animals": animais})
