import os
from django.http import HttpResponse
from django.views.generic import TemplateView


class ProfilesData(TemplateView):
    template_name = 'perfiles/profile.html'


def resume_view(request):
    url_resume = request.user.perfil.cv.url
    cd = os.getcwd() + '{}'
    dir_resume = cd.format(url_resume)
    print(dir_resume)
    with open(dir_resume, 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=cv.pdf'
        return response

