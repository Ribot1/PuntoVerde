from django.contrib import admin
from .models import InventarioContenedores,LlenadoContenedores,Boleta,Comprador,ContenedorLleno,DetaAsignacion,Empleado,Factura,Informe,IngresoMaterial,Receptor,Reserva,Retiro,Compra
# Register your models here.

class ingreso(admin.ModelAdmin):
    list_display = ["id_material","tipo_producto","fecha","pesos_material"]
    list_editable =["pesos_material"]
    list_filter = ["tipo_producto"]

class lcontenedor(admin.ModelAdmin):
    list_display = ["id_llenado","tipo_contenedor","peso","estado_contenedor","precio"]
    list_editable =["peso","precio"]
    list_filter = ["tipo_contenedor"]

class ncontenedor(admin.ModelAdmin):
    list_display = ["id_contenedor","tipo_contenedor","peso","id_llenado"]
    list_editable =["tipo_contenedor","peso"]
    list_filter = ["tipo_contenedor"]

admin.site.register(Boleta)
admin.site.register(Comprador)
admin.site.register(LlenadoContenedores,lcontenedor)
admin.site.register(ContenedorLleno)
admin.site.register(DetaAsignacion)
admin.site.register(InventarioContenedores,ncontenedor)
admin.site.register(Empleado)
admin.site.register(Factura)
admin.site.register(Informe)
admin.site.register(IngresoMaterial,ingreso)
admin.site.register(Receptor)
admin.site.register(Reserva)
admin.site.register(Retiro)
admin.site.register(Compra) 

