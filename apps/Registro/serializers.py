from rest_framework import serializers
from .models import Recomendacion

class RecomendacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recomendacion
        fields = ('id', 'nombre', 'email', 'producto', 'telefono', 'razon')