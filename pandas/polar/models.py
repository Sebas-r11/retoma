from django.db import models

class ingreso(models.Model):
    fecha = models.DateField()
    cantidad = models.IntegerField()
    proveedor = models.CharField(max_length=50)

    def __str__(self):
        return self.producto