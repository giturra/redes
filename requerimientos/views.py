from django.views.generic import FormView
from django.forms import ValidationError
from .forms import RequirementForm
from .models import Requerimiento, Producer


class Requirement(FormView):
    template_name = "requerimientos/requerimientos.html"
    form_class = RequirementForm
    success_url = '/'

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