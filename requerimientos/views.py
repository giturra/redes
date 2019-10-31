from django.views.generic import TemplateView


class RequirementForm(TemplateView):
    template_name = "requerimientos/add_postin.html"
