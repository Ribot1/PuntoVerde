from django import forms
from django.forms import ModelForm,widgets 
from .models import IngresoMaterial

class IngresarForm(ModelForm):

    class Meta:
        model = IngresoMaterial
        fields = ['id_material','tipo_producto','fecha','pesos_material','receptor_rut_receptor','contenedor_id_contenedor']

        labels={
            'id_material':"id_Material:",
            'tipo_producto': "Tipo:",
            'fecha' : "Fecha:",
            'pesos_material': "Peso:",
            'receptor_rut_receptor': "Receptor",
            'contenedor_id_contenedor' : "Contenedor:"
        }

        widgets={
            'id_material':forms.NumberInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'material', 
                    'name': 'material',
                    'placeholder': 'ingreso_material'
                }
            ),
            
            'tipo_producto':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'producto', 
                    'name': 'producto',
                    'placeholder': 'tipo'
                }
            ),
            'fecha':forms.DateInput(
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
            'receptor_rut_receptor':forms.TextInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'rut', 
                    'name': 'rut',
                    'placeholder': 'rut'
                }
            ),
            'contenedor_id_contenedor':forms.NumberInput(
                attrs={
                    'class': 'form-titulo',
                    'id': 'contenedor', 
                    'name': 'contenedor',
                    
                }
            ),
            
        }
