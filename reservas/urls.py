from django.urls import path
from .views import CompaniesList, CompaniesDetail

urlpatterns = [
    path('empresas/', CompaniesList.as_view(), name='companies'),
    path('empresa/<int:pk>/', CompaniesDetail.as_view(), name='detail')
]