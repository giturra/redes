from django.views.generic import TemplateView
from .forms import ExampleForm


class RequirementForm(TemplateView):
    template_name = "requerimientos/requerimientos.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        if "form" not in kwargs:
            kwargs['form'] = ExampleForm()
            return super().get(request, *args, **kwargs)