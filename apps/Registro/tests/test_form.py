from django.test import TestCase
from apps.Registro.models import Recomendacion
from apps.Registro.forms import RecomendacionesForm

class RecomendacionFormCase(TestCase):
        
    def test_valid_form(self):
        # fields = ['nombre', 'email', 'telefono', 'producto', 'razon']
        recomendacion = Recomendacion.objects.create(nombre="Angel",email="guero0103.05@gmail.com",telefono="10000" ,producto="Chiptop",razon="Lo necesito")
        data = {'nombre': recomendacion.nombre, 'email': recomendacion.email,'telefono': recomendacion.telefono,'producto': recomendacion.producto,'razon': recomendacion.razon, }
        form = RecomendacionFormCase(data=data)
        self.assertTrue(form.is_valid())
        
    def test_invalid_form(self):
        recomendacion = Recomendacion.objects.create(nombre="Alejo",email="alejo003@gmail.com",telefono="984752613" ,producto="Chipsuyu",razon="Lo necesito")
        data = {'nombre': recomendacion.nombre, 'email': recomendacion.email,'telefono': recomendacion.telefono,'producto': recomendacion.producto,'razon': recomendacion.razon, }
        form = RecomendacionFormCase(data=data)
        self.assertTrue(form.is_valid())