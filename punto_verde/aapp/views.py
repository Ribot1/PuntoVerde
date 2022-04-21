from django import forms
from django.forms.forms import Form
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.


def home(request):
   return render(request, 'app/home.html')


def registro(request):
   return render(request, 'app/registro.html')

def estado(request):
   return render(request, 'app/estado.html')

def recicla(request):
   return render(request, 'app/recicla.html')

def llenado(request):
   return render(request, 'app/llenado.html')

def mostrar(request):
    deposit= IngresoMaterial.objects.all()
    return render(request,'app/ingreso.html',{'deposit':deposit})