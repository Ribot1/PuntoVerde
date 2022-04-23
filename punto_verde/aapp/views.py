from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.forms.forms import Form
from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db import connection
import cx_Oracle
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



def agregar_usuario(username, nombre, apellido, correo, clave):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.number)
    cursor.callproc('SP_AGREGAR_USUARIO',[username, nombre, apellido, correo, clave, salida]) 
    return salida.getvalue()


def registro2(request):

    #agregar_usuario
    if request.method == 'POST':
        username = request.POST.get('username')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        clave = request.POST.get('clave')
        salida = agregar_usuario(username, nombre, apellido, correo, clave)
        if salida == 1:
            print ('se ha registrado el usuario')
        else:
            print ('no se ha podido guardar')

    return render(request, 'app/registration/registro2.html')