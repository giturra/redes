from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path


urlpatterns = [
    path('ingresar/', LoginView.as_view(template_name="perfiles/login.html"), name='login'),
    path('salir/', LogoutView.as_view(), name='logout')
]
