from django.urls import path
from .views import Requirement, QuotaRequirement

urlpatterns = [
    path('', Requirement.as_view(), name='form_req'),
    path('cupos/', QuotaRequirement.as_view(), name='form-cupos')
]