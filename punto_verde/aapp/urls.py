from django.urls import path
from.views import home, registro

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),


]
