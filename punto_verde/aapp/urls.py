from django.conf import settings
from django.urls import path
from . import views
from.views import  *
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
    path('recicla/', recicla, name="recicla"),
    path('llenado/', llenado, name="llenado"),
    path('mostrar/',views.mostrar,name="mostrar"),
    path('estado/',views.estado, name='estado'),
    path('ingreso/',views.ingreso , name='ingreso'),
    path('asignacion',asignacion,name="asignacion"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

