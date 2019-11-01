from django.db import models


class Requerimiento(models.Model):
    nombre_empresa = models.CharField("Nombre Compañia", max_length=150)
    descripcion = models.TextField("Descripción", max_length=5000)
    representante = models.CharField("Nombre de la persona de su empresa a cargo de la Feria", max_length=150)
    celular = models.CharField("Celular de la persona de su empresa a cargo de la Feria", max_length=12)
    email = models.EmailField("Email de la persona de su empresa a cargo de la Feria", max_length=150)
    dia_asistencia = models.CharField(max_length=100)
    tipo_stand = models.CharField(max_length=100)
    stand_propio = models.BooleanField()
    entrevistadores = models.IntegerField()
    almuerzos_normales = models.IntegerField()
    almuerzos_vegetarianos = models.IntegerField()
