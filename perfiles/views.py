import os
from .models import Perfil
from django.urls import reverse_lazy
from .forms import ProfileForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
 

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

class Profile(View):
    profile_form = ProfileForm()
    context = {
        'form':profile_form
    }
    template_name = 'perfiles/profile.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        self.context['user'] = user
        return render(request, self.template_name, self.context)
    
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        self.context['user'] = user
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
        return render(request, self.template_name, context=self.context)
# class Profile(UpdateView):
#     model = Perfil
#     success_url = reverse_lazy('/')
#     fields = ['__all__']
#     slug_field = 'username'
#     slug_url_kwarg = 'username'