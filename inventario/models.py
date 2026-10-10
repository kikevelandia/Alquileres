from django.db import models


class Cliente(models.Model):
    id_cliente = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=30)

    class Meta:
        db_table = "cliente"

    def __str__(self):
        return f"{self.nombre} ({self.id_cliente})"


class Stock(models.Model):
    id_producto = models.CharField(max_length=4, primary_key=True)
    nombre = models.CharField(max_length=15)
    tipo = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    acciones = models.CharField(max_length=30)

    class Meta:
        db_table = "stock"

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class Evento(models.Model):
    id_evento = models.CharField(max_length=4, primary_key=True)
    fecha = models.DateTimeField()
    direccion = models.CharField(max_length=30)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        db_column="id_cliente",
        related_name="eventos",
    )

    class Meta:
        db_table = "evento"

    def __str__(self):
        return f"Evento {self.id_evento} - {self.fecha:%d/%m/%Y}"


class DetalleEvento(models.Model):
    id_detalle = models.CharField(max_length=4, primary_key=True)
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        db_column="id_evento",
        related_name="detalles",
    )
    producto = models.ForeignKey(
        Stock,
        on_delete=models.PROTECT,
        db_column="id_producto",
        related_name="detalles",
    )
    cantidad = models.IntegerField()

    class Meta:
        db_table = "detalle_evento"

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} (evento {self.evento_id})"


class Pago(models.Model):
    id_pago = models.CharField(max_length=15, primary_key=True)
    evento = models.ForeignKey(
        Evento,
        on_delete=models.CASCADE,
        db_column="id_evento",
        related_name="pagos",
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateField()

    class Meta:
        db_table = "pagos"

    def __str__(self):
        return f"Pago {self.id_pago} - {self.total}"

# Create your models here.
