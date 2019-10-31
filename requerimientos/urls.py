from django.urls import path
from .views import RequirementForm

urlpatterns = [
    path('', RequirementForm.as_view())
]