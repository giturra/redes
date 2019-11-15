from django.shortcuts import render
from .models import Empresa
from django.views.generic import ListView, TemplateView


class CompaniesList(ListView):
    template_name = 'reservas/empresas.html'
    queryset = Empresa.objects.all()
    context_object_name = 'empresas'


class CompaniesDetail(TemplateView):
    template_name = 'reservas/detalle-empresa.html'

