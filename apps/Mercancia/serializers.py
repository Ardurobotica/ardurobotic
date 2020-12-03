from rest_framework import serializers
from .models import Mercancia

class MercanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercancia
        fields = '__all__'
