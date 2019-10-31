from django.db import models
from django.contrib.auth.models import User


class Carrera(models.Model):
    plan = models.CharField(max_length=150)

    def __str__(self):
        return self.plan


class Empleo(models.Model):
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo


def user_cv_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/cv/user_<id>/<filename>
    return 'cv/user_{0}/{1}'.format(instance.usuario.id, filename)


def user_foto_perfil_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/cv/user_<id>/<filename>
    return 'foto_perfil/user_{0}/{1}'.format(instance.usuario.id, filename)


class Perfil(models.Model):

    class Meta:
        verbose_name_plural = 'Perfiles'

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    egresado = models.BooleanField()
    rut = models.CharField(max_length=20)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    empleo = models.ForeignKey(Empleo, on_delete=models.CASCADE)
    cv = models.FileField(upload_to=user_cv_path, null=False)
    foto_perfil = models.ImageField(upload_to=user_foto_perfil_path, null=False)
    perfil_pro = models.TextField(max_length=500)
    fecha_union = models.DateTimeField(auto_now_add=True)
    ano_ingreso = models.IntegerField()
    ano_egreso = models.IntegerField()
    ultima_conex = models.DateTimeField(auto_now=True)
    spam = models.BooleanField()
    eula = models.BooleanField()




