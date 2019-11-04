from django.views.generic import FormView
from .forms import RequirementForm


class Requirement(FormView):
    template_name = "requerimientos/requerimientos.html"
    form_class = RequirementForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        print("")
        return super().form_valid(form)