from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfilesData, resume_view
from django.urls import path


urlpatterns = [
    path('ingresar/', LoginView.as_view(template_name="perfiles/login.html"), name='login'),
    path('salir/', LogoutView.as_view(), name='logout'),
    path('perfil/', ProfilesData.as_view(), name='profile'),
    path('ver_cv/', resume_view, name='cv')
]

