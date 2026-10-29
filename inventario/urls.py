from django.urls import path, include
from rest_framework import routers
from .views import (
    ClienteViewSet, StockViewSet, EventoViewSet,
    DetalleEventoViewSet, PagoViewSet,
)

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('stock', StockViewSet)
router.register('eventos', EventoViewSet)
router.register('detalles', DetalleEventoViewSet)
router.register('pagos', PagoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]