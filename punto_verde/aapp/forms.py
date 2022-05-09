from dataclasses import fields
from pyexpat import model
from django import forms
from .models import *


class Conchetumare(forms.ModelForm):

    class Meta:
        model = IngresoMaterial
        fields = "__all__"
        # fields = ["id_material","tipo_producto","fecha","peso_material"]

    
class ingreform(forms.ModelForm):
    class Meta:
        model = IngresoMaterial
        fields = '__all__' 
        labels={
            'id_material': 'id_material:',
            'tipo_producto': 'tipo_producto:', 
            'fecha': 'fecha:',
            'pesos_material': 'pesos_material:',
            'llen_conts_id_llenado': 'contenedores',
        }
        Widgets={
            'id_material':forms.NumberInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'material', 
                    'name': 'material',
                    'placeholder': 'id'
                }
            ),
            'tipo_producto':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'tipo', 
                    'name': 'tipo',
                    'placeholder': 'ingresar_rut'
                }
            ),
            'fecha':forms.DateTimeInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'fecha', 
                    'name': 'fecha',
                    'placeholder': 'fecha'
                }
            ),
            'pesos_material':forms.NumberInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'peso', 
                    'name': 'peso',
                    'placeholder': 'peso'
                }
            ),
            'llen_conts_id_llenado':forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'contenedor', 
                    'name': 'contenedor',
                    'placeholder': 'contenedores'
                }
            ),}

class llenandoForm(forms.ModelForm):
        class Meta:
            model = LlenadoContenedores
            fields = '__all__'
            labels={
                'id_llenado': 'id_material:',
                'tipo_contenedor': 'tipo_producto:', 
                'peso': 'peso:',
                'estado_contenedor': 'estado:',
                'precio': 'precio',
                'invt_conts_id_contenedor': 'inventario',
                'ingreso_material_id_material': 'material',
            }
            Widgets={
                'id_llenado':forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'id': 'id_llenado', 
                        'name': 'id_llenado',
                        'placeholder': 'id'
                    }
                ),
                'tipo_contenedor':forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'id': 'tipo', 
                        'name': 'tipo',
                        'placeholder': 'tipo_contenedor'
                    }
                ),
                'peso':forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'id': 'peso', 
                        'name': 'peso',
                        'placeholder': 'peso'
                    }
                ),
                'estado_contenedor':forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'id': 'estado', 
                        'name': 'estado',
                        'placeholder': 'estado'
                    }
                ),
                'precio':forms.NumberInput(
                    attrs={
                        'class': 'form-control',
                        'id': 'precio', 
                        'name': 'precio',
                        'placeholder': 'precio'
                    }
                ),
                'invt_conts_id_contenedor':forms.Select(
                   attrs={
                       'class': 'form-control',
                        'id': 'contenedor', 
                        'name': 'contenedor',
                        'placeholder': 'contenedores'
                   }     
                ),
                'ingreso_material_id_material':forms.Select(
                    attrs={
                       'class': 'form-control',
                        'id': 'ingreso', 
                        'name': 'ingreso',
                        'placeholder': 'ingreso'
                   }     
                ),

                }