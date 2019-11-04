from django.db import models


class Carrera(models.Model):
    plan = models.CharField(max_length=150)

    def __str__(self):
        return self.plan


class Empleo(models.Model):
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo
