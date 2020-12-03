from django import forms
from .models import Recomendacion

class RecomendacionesForm(forms.ModelForm):
    class Meta:
        model = Recomendacion
        fields = ['nombre', 'email', 'producto', 'telefono', 'razon']

        labels = {
            'nombre': 'Nombre',
            'email': 'Email',
            'producto': 'Producto',
            'telefono': 'Telefono',
            'razon': 'Razon',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'producto': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'razon': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
