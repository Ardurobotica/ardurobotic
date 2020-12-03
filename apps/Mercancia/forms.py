from .models import Mercancia
from django import forms

class MercanciaForm(forms.ModelForm):
    

    class Meta:
        model = Mercancia
        fields = (
            'fotografia',
            'nombre',
            'descripcion',
            'precio'
        )
        labels = {
            'fotografia':'Fotografia',
            'nombre':'Nombre',
            'descripcion':'Descripcion',
            'precio':'Precio'
            }
        widgets = {
            # 'fotografia':forms.FileInput(attrs={'class':'form-control','type':'file'}),
            'rut':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'grado_academico':forms.Select(choices="GRADOS_ACADEMICO", attrs={'class':'form-control'}),
        }
