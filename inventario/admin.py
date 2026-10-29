from django.contrib import admin
from .models import Cliente, Stock, Evento, DetalleEvento, Pago

admin.site.register([Cliente, Stock, Evento, DetalleEvento, Pago])