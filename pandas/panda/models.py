from django.db import models

class produccion(models.Model):
        seccion = models.CharField(max_length=11)
        dia = models.DateField(auto_now_add=True)
        produccion = models.IntegerField()

        def __str__(self):
            return self.seccion + ' ' + self.produccion
        

