from django.test import TestCase
from django.template.defaultfilters import slugify
from apps.Registro.models import Recomendacion

class RecomendacionTestCase(TestCase):
    def setUp(self):
        Recomendacion.objects.create(nombre="Angel",email="guero0103.05@gmail.com",producto="Chiptop" ,telefono="10000",razon="Lo necesito")
        Recomendacion.objects.create(nombre="Alejo",email="alejo003@gmail.com",producto="Chipsuyu" ,telefono="984752613",razon="Lo necesito")

    def test_ingresar_mensajes(self):
        """Los mensajes se registran correctamente en la BD"""
        Recomendacion_1 = Recomendacion.objects.get(nombre="Angel")
        Recomendacion_2 = Recomendacion.objects.get(nombre="Alejo")
        self.assertEqual(Recomendacion_1.telefono, "10000")
        self.assertEqual(Recomendacion_2.telefjono, "984752613")
