from django.urls import path
from .views import Requirement

urlpatterns = [
    path('', Requirement.as_view(), name='form_req')
]