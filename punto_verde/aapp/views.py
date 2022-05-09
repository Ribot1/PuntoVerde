from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.forms.forms import Form
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db import connection
# Create your views here.


def home(request):
   return render(request, 'app/home.html')


def registro(request):
   return render(request, 'app/registro.html')

def estado(request):
   # ---Trae informacion de models.py Contenedor
   contenedor = LlenadoContenedores.objects.all()
 
   return render(request, 'app/estado.html', {'contenedor': contenedor  })

def recicla(request):
   data={
      'form': Conchetumare()

   }
   if request.method =='POST':
      formulario = Conchetumare(data=request.POST)
      if formulario.is_valid():
         formulario.save()
         data["mensaje"] = "se guardo"
      else:
         data['form'] = formulario


   return render(request, 'app/recicla.html',data)

def llenado(request):


   return render(request, 'app/llenado.html')



def ingreso(request):
   # ---Trae informacion de models.py  IngresoMaterial
    ingresos = IngresoMaterial.objects.all()
    print(ingresos)
    return render(request,'app/prueba.html', {'ingresos':ingresos} )


def mostrar(request): 
  # ---Trae informacion de models.py  Contenedor
    contenedor = LlenadoContenedores.objects.all()

 

    return render(request,'app/ingreso.html',{'contenedor': contenedor }, )

llenando = llenandoForm()
def asignacion(request):
   global llenando 
   data={
      'form': llenandoForm()

   }
   if request.method =='POST':
      llenando = llenandoForm(request.POST, request.FILES)
      if llenando.is_valid():
         llenando.save()
         data["mensaje"] = "se guardo"
         return redirect('estado')
      else:
         data['form'] = llenando


   return render(request, 'app/asignar.html',{'llenando':llenando})


