from django.db import models

class examen(models.Model):
    cliente = models.CharField(max_length=50);
    vuelo = models.CharField(max_length=50);
    fecha_salida = models.DateField();
    fecha_entrada = models.DateField();

    def __str__(self):
        return self.cliente
    
