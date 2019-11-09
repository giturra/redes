from .choices import BRING_STAND_CHOICES, DAY_CHOICES, STAND_CHOICES, STAND_TYPE_CHOICES, TIPOS_ENTREVISTAS
from django.db import models
from app.models import Carrera, Empleo


class Requerimiento(models.Model):

    nombre_empresa = models.CharField("Nombre Compañia", max_length=150)
    descripcion = models.TextField("Descripción", max_length=5000)
    representante = models.CharField("Nombre de la persona de su empresa a cargo de la Feria", max_length=150)
    celular = models.CharField("Celular de la persona de su empresa a cargo de la Feria", max_length=12)
    email = models.EmailField("Email de la persona de su empresa a cargo de la Feria", max_length=150)
    dia_asistencia = models.CharField("Día de Participación", max_length=5, choices=DAY_CHOICES)
    tipo_stand = models.CharField("Tipo de Stand", max_length=5, choices=STAND_TYPE_CHOICES)
    stand_propio = models.CharField("¿Utilizará Stand Propio o Stand Feria?", max_length=5, choices=BRING_STAND_CHOICES)
    stand1 = models.CharField("Stand de Preferencia 1", max_length=2, choices=STAND_CHOICES)
    stand2 = models.CharField("Stand de Preferencia 2", max_length=2, choices=STAND_CHOICES)
    stand3 = models.CharField("Stand de Preferencia 3", max_length=2, choices=STAND_CHOICES)
    entrevistadores = models.IntegerField()
    almuerzos_normales = models.IntegerField(default=0)
    almuerzos_vegetarianos = models.IntegerField(default=0)
    tipo_entrevista = models.CharField("Tipo entrevistas", max_length=2, choices=TIPOS_ENTREVISTAS)
    tiempo_entrevista = models.IntegerField(default=15)
    formato_entrevista = models.TextField("Describa el formato de entrevista", max_length=5000, null=True)

    # to do agregar una validación dinámica if una cantidad de almuerzos tiene un máximo la otra debe ser 0

    def __str__(self):
        return self.nombre_empresa
    


class Producer(models.Model):
    nombre = models.CharField(max_length=100)
    persona = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    requerimiento = models.ForeignKey(Requerimiento, on_delete=models.CASCADE)


class Cupos(models.Model):
    carrera = models.ManyToManyField(Carrera)
    plan = models.ManyToManyField(Empleo)
    cupos = models.IntegerField()
    requerimiento = models.ForeignKey(Requerimiento, on_delete=models.CASCADE)