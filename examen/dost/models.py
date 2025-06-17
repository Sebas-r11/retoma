from django.db import models

class tabdos(models.Model):
    nombre_usuario = models.CharField(max_length=100);
    correo_electronico = models.EmailField();
    password = models.CharField(max_length=100);
    fecha_creacion = models.DateField();

    def __str__(self):
        return self.nombre_usuario;
