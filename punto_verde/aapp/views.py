from django.shortcuts import render

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