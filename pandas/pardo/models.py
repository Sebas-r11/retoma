from django.db import models

class calificador(models.Model):
    proveedor = models.CharField(max_length=100)
    muestra = models.IntegerField()
    aprovados = models.IntegerField()
    rechazados = models.IntegerField()
    
    def __str__(self):
        return self.proveedor