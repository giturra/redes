from redes.settings import EMAIL_HOST_USER
from django.shortcuts import render
from django.core.mail import EmailMessage, send_mail
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "index.html"


class Contact(TemplateView):
    template_name = "app/contact.html"
    http_method_names = ['get', 'post']

    def post(self, request, *args, **kwargs):
        name = request.POST['name-form']
        email = request.POST['email-form']
        subject = request.POST['subject-form']
        message = request.POST['message-form']
        msg = "Mensaje enviado desde Contacto Pagina Web \n" + "Nombre: " + name + "\n" + "Email: " + email + "\n" + "Mensaje: " + message
        send_mail(
            "Mensaje enviado desde Contacto Pagina Web", 
            msg, 
            EMAIL_HOST_USER, 
            [EMAIL_HOST_USER], 
            fail_silently=False)
        return render(request, self.template_name)
        


