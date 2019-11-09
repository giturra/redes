from django.db import models
from app.models import Carrera, Empleo
from django.contrib.auth.models import User
from app.models import Carrera, Empleo


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
    cv = models.FileField("Curriculum Vitae", upload_to=user_cv_path, null=False)
    foto_perfil = models.ImageField("Foto de Perfil", upload_to=user_foto_perfil_path, null=False)
    perfil_pro = models.TextField("Descripción Profesional", max_length=500)
    fecha_union = models.DateTimeField(auto_now_add=True)
    ano_ingreso = models.IntegerField("Año de Ingreso")
    ano_egreso = models.IntegerField("Año de Egreso")
    ultima_conex = models.DateTimeField(auto_now=True)
    spam = models.BooleanField()
    eula = models.BooleanField()




