from django.db import models

class TabTrest(models.Model):
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    post_id = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_usuario;