import os
from .models import Perfil
from django.urls import reverse_lazy
from .forms import ProfileForm
from .models import Perfil
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
 

# class ProfilesData(FormView):
#     template_name = 'perfiles/profile.html'
#     form_class = ProfileForm
#     success_url = '/perfiles/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# def resume_view(request):
#     url_resume = request.user.perfil.cv.url
#     cd = os.getcwd() + '{}'
#     dir_resume = cd.format(url_resume)
#     print(dir_resume)
#     with open(dir_resume, 'r') as pdf:
#         response = HttpResponse(pdf.read(), mimetype='application/pdf')
#         response['Content-Disposition'] = 'inline;filename=cv.pdf'
#         return response

# class Profile(View):
#     profile_form = ProfileForm()
#     context = {
#         'form':profile_form
#     }
#     template_name = 'perfiles/profile.html'

#     def get(self, request, *args, **kwargs):
#         user = User.objects.get(username=request.user.username)
#         self.context['user'] = user
#         return render(request, self.template_name, self.context)
    
#     def post(self, request, *args, **kwargs):
#         user = User.objects.get(username=request.user.username)
#         self.context['user'] = user
#         profile_form = ProfileForm(request.POST)
#         if profile_form.is_valid():
#             profile_form.save()
#         return render(request, self.template_name, context=self.context)
# class Profile(UpdateView):
#     model = Perfil
#     success_url = reverse_lazy('/')
#     fields = ['__all__']
#     slug_field = 'username'
#     slug_url_kwarg = 'username'

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
