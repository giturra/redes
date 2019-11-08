from .models import Perfil
from .forms import ProfileForm
from .models import Perfil
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class Profile(LoginRequiredMixin, TemplateView):
    template_name = "perfiles/profile.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        perfil = Perfil.objects.get(usuario=user)
        kwargs['form'] = ProfileForm(instance=perfil)
        return super(Profile, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        user = self.request.user
        perfil = Perfil.objects.get(usuario=user)
        form = ProfileForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
        return redirect('/perfil/')
