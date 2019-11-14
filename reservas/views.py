from django.shortcuts import render
from django.views.generic import TemplateView


class CompaniesList(TemplateView):
    template_name = 'reservas/empresas.html'


class CompaniesDetail(TemplateView):
    template_name = 'reservas/detalle-empresa.html'

