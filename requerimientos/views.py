from django.shortcuts import redirect
from django.views.generic import FormView, ListView
from django.forms import ValidationError
from .forms import RequirementForm
from .models import Requerimiento, Producer
from app.models import Carrera


class Requirement(FormView):
    template_name = "requerimientos/requerimientos.html"
    form_class = RequirementForm
    success_url = '/requerimientos/cupos'

    def form_valid(self, form):
        prod = form.cleaned_data['productora_nombre']
        per = form.cleaned_data['persona_nombre']
        con = form.cleaned_data['productora_contacto']
        email = form.cleaned_data['productora_email']
        req = form.save()
        if (prod and per and con and email):
            Producer.objects.create(
                nombre=prod,
                persona=per,
                contacto=con,
                email=email,
                requerimiento=req
            )
        return super().form_valid(form)


class QuotaRequirement(ListView):
    template_name = "requerimientos/requerimientos-cupos.html"
    model = Carrera
    context_object_name = "carreras"
    http_method_names = ['get', 'post']

    def post(self, request, *args, **kwargs):
        for key, value in request.POST.items():
            print(key, value)
        return redirect('/requerimientos/cupos/')

    
    