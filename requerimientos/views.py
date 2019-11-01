from django.views.generic import TemplateView
from .forms import RequirementForm


class Requirement(TemplateView):
    template_name = "requerimientos/requerimientos.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        if "form" not in kwargs:
            kwargs['form'] = RequirementForm()
            return super(Requirement, self).get(request, *args, **kwargs)