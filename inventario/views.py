from rest_framework import viewsets
from .models import Cliente, Stock, Evento, DetalleEvento, Pago
from .serializers import (
    ClienteSerializer, StockSerializer, EventoSerializer,
    DetalleEventoSerializer, PagoSerializer,
)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class DetalleEventoViewSet(viewsets.ModelViewSet):
    queryset = DetalleEvento.objects.all()
    serializer_class = DetalleEventoSerializer


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer