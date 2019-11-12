from django.urls import path
from .views import Index, Contact

urlpatterns = [
    path('', Index.as_view()),
    path('contacto/', Contact.as_view(), name='contact')
]