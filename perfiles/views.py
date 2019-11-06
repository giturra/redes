import os
from .models import Perfil
from .forms import ProfileForm, UserForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.models import User 

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
    user_form = UserForm()
    profile_form = ProfileForm()
    context = {
        'user_form':user_form, 'profile_form':profile_form
    }
    template_name = 'perfiles/profile.html'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        self.context['user'] = user
        return render(request, self.template_name, self.context)