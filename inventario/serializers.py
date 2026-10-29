from rest_framework import serializers
from .models import Cliente, Stock, Evento, DetalleEvento, Pago

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        

        
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
        
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


class DetalleEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleEvento
        fields = '__all__'


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'                            