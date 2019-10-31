from django.db import models


class Requerimiento(models.Model):
    nombre_empresa = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    representante = models.CharField(max_length=150)
    celular = models.CharField(max_length=12)
    email = models.CharField(max_length=150)
    dia_asistencia = models.CharField(max_length=100)
    tipo_stand = models.CharField(max_length=100)
    stand_propio = models.BooleanField()
    entrevistadores = models.IntegerField()
    almuerzos_normales = models.IntegerField()
    almuerzos_vegetarianos = models.IntegerField()
