from django.db import models
from django.contrib.auth.models import User


class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    creacion = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True)
    importancia = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class SubTarea(models.Model):
    descripcion = models.TextField(blank=True)
    eliminada = models.BooleanField(default=False)
    tarea_id = models.ForeignKey(Tarea, on_delete=models.CASCADE)
