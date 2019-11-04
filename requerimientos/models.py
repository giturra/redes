from django.db import models


class Requerimiento(models.Model):
    DAY_CHOICES = (
        ('1', 'Lunes (07/10/2020)'),
        ('2', 'Martes (08/10/2020)'),
        ('3', 'Miércoles (09/10/2020)'),
    )
    STAND_TYPE_CHOICES = (
        ('1', 'Stand simple (3m x 3m)'),  # 2
        ('2', 'Stand especial 4 (4m x 3m)'),  # 3
        ('3', 'Stand especial 5 (5m x 3m)'),  # 4
        ('4', 'Stand doble (6m x 3m)'),  # 4
    )
    BRING_STAND_CHOICES = (
        ('True', 'Stand Propio'),
        ('False', 'Stand Feria'),
    )
    STAND_CHOICES = (
        ('A', 'Stand A'),
        ('B', 'Stand B'),
        ('1', 'Stand 1'),
        ('2', 'Stand 2'),
        ('3', 'Stand 3'),
        ('4', 'Stand 4'),
        ('5', 'Stand 5'),
        ('6', 'Stand 6'),
        ('7', 'Stand 7'),
        ('8', 'Stand 8'),
        ('9', 'Stand 9'),
    )
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
    entrevistadores = models.IntegerField(null=True)
    almuerzos_normales = models.IntegerField(null=True)
    almuerzos_vegetarianos = models.IntegerField(null=True)
    tipo_entrevista = models.CharField("Tipo entrevistas", max_length=2)
    tiempo_entrevista = models.IntegerField(default=15)
    formato_entrevista = models.TextField("Describa el formato de entrevista", max_length=5000)