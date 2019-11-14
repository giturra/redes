from app.models import Carrera, Empleo
from perfiles.models import Perfil
from django.db import models

class Empresa(models.Model):

    OPCIONES_EMPRESAS = (
        (0, "Privada"),
        (1, "Invitada"),
    )

    tipo_empresa = models.IntegerField(choices=OPCIONES_EMPRESAS)
    logo = models.ImageField(upload_to='logos/', null=True)
    #ofertas = models.TextField()  # supongo que vamos a guardar el json como string?
    descripcion = models.TextField(max_length=1000)
    web = models.URLField()
    fb = models.URLField()
    lkin = models.URLField()
    ig = models.URLField()
    twt = models.URLField()
    rut = models.CharField(max_length=20)
    nombre = models.CharField(max_length=200)
    #encuesta = models.URLField()

    def __str__(self):
        return self.nombre


class ImagenEmpresa(models.Model):
    imagen = models.ImageField(upload_to='imagenes/', null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

# class Oferta(models.Model):
#     cargo = models.CharField(max_length=150)
#     direccion = models.CharField(max_length=200)
#     duracion = models.CharField(max_length=150)
#     descripcion = models.TextField(max_length=500)
#     requisitos =  models.TextField(max_length=500)
#     remuneracion = models.CharField(max_length=200)
#     fecha = models.DateField(default=datetime.today())
#     empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.cargo + " - " + self.empresa.nombre


class EspecialidadOferta(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    #oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)


class EmpleoOferta(models.Model):
    empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE)
    #oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)


class Entrevista(models.Model):
    hora_inicio = models.DateTimeField(unique=True, auto_now=False, auto_now_add=False)
    hora_cierre = models.DateTimeField(unique=True, auto_now=False, auto_now_add=False)
    entrevistados = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    #oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    OPCIONES_ASISTENCIA = (
        (0, "Si"),
        (1, "No"),
        (2, "Pendiente")
    )
    asistencia = models.IntegerField(choices=OPCIONES_ASISTENCIA)
    ocupado = models.BooleanField(default=False)
