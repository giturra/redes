from django.urls import path
from .views import Requirement, QuotaRequirement, cupos_carreras

urlpatterns = [
    path('', Requirement.as_view(), name='form_req'),
    path('cupos/', QuotaRequirement.as_view(), name='form-cupos'),
    path('cupos/guardar/', cupos_carreras, name='form-cupos-guardar')
]