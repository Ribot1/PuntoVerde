from django.urls import path
from.views import  estado, home, llenado, recicla, registro

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
    path('estado/', estado, name="estado"),
    path('recicla/', recicla, name="recicla"),
    path('llenado/', llenado, name="llenado"),


]
