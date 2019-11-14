from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView
from django.forms import ValidationError
from .forms import RequirementForm
from .models import Cupos, Requerimiento, Producer
from app.models import Carrera, Empleo


class Requirement(FormView):
    template_name = "requerimientos/requerimientos.html"
    form_class = RequirementForm
    success_url = '/requerimientos/cupos'

    def form_valid(self, form):
        #print(form)
        prod = form.cleaned_data['productora_nombre']
        per = form.cleaned_data['persona_nombre']
        con = form.cleaned_data['productora_contacto']
        email = form.cleaned_data['productora_email']
        entrevistadores = form.cleaned_data['entrevistadores']
        tiempo = form.cleaned_data['tiempo_entrevista']
        req = form.save()
        if (prod and per and con and email):
            Producer.objects.create(
                nombre=prod,
                persona=per,
                contacto=con,
                email=email,
                requerimiento=req
            )
        response = super().form_valid(form)
        response.set_cookie('req_id', req.id)
        return response


class QuotaRequirement(ListView):
    template_name = "requerimientos/requerimientos-cupos-carreras.html"
    model = Carrera
    context_object_name = "carreras"
    http_method_names = ['get', 'post']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        req_id = self.request.COOKIES.get('req_id')
        req = Requerimiento.objects.get(id=req_id)
        entrevistadores = req.entrevistadores
        tiempo = req.tiempo_entrevista
        cupos = int(26 * (15 / tiempo) * entrevistadores)
        context['cupos'] = cupos
        return context
    
    # def post(self, request, *args, **kwargs):
    #     for key, value in request.POST.items():
    #         print(key, value)
    #     return redirect('/')


def cupos_carreras(request):

    if request.method == "POST":
        print("holaaaaaaaaaaaaa")
        carreras_restantes = int(request.POST["n_carreras"])
        carrera_actual = 1
        while carreras_restantes > 0:
            #print(models.CuposCarrera.objects.all())
            nombre_carrera = "carrera_" + str(carrera_actual)
            carrera_id = request.POST.get(nombre_carrera)
            if carrera_id is not None:
                print(carrera_actual)
                #print(carrera)
                p1 = request.POST.get("prctica1_" + str(carrera_actual), 0)
                p2 = request.POST.get("prctica2_" + str(carrera_actual), 0)
                p3 = request.POST.get("prctica3_" + str(carrera_actual), 0)
                me = request.POST.get("memoria_" + str(carrera_actual), 0)
                pt = request.POST.get("parttime_" + str(carrera_actual), 0)
                ft = request.POST.get("fulltime_" + str(carrera_actual), 0)
                #pt = request.POST.get(u'_'.join(("parttime", carrera_actual)), 0)

                carrera = Carrera.objects.get(id=carrera_id)
                print(p1)
                requirement_id = request.COOKIES.get('req_id')
                #print(requirement_id)
                requirement = Requerimiento.objects.get(id=requirement_id)

                if p1 and p1 != 0:
                    plan = Empleo.objects.get(id=1)
                    p1_data = Cupos(cupos=p1, requerimiento=requirement)
                    p1_data.save()
                    p1_data.carrera.add(carrera)
                    p1_data.plan.add(plan)
                if p2 and p2 != 0:
                    plan = Empleo.objects.get(id=2)
                    p2_data = Cupos(cupos=p2, requerimiento=requirement)
                    p2_data.save()
                    p2_data.carrera.add(carrera)
                    p2_data.plan.add(plan)
                if p3 and p3 != 0:
                    plan = Empleo.objects.get(id=3)
                    p3_data = Cupos(cupos=p3, requerimiento=requirement)
                    p3_data.save()
                    p3_data.carrera.add(carrera)
                    p3_data.plan.add(plan)
                if me and me != 0:
                    plan = Empleo.objects.get(id=4)
                    me_data = Cupos(cupos=me, requerimiento=requirement)
                    me_data.save()
                    me_data.carrera.add(carrera)
                    me_data.plan.add(plan)
                if pt and pt != 0:
                    plan = Empleo.objects.get(id=5)
                    pt_data = Cupos(cupos=pt, requerimiento=requirement)
                    pt_data.save()
                    pt_data.carrera.add(carrera)
                    pt_data.plan.add(plan)
                if ft and ft != 0:
                    plan = Empleo.objects.get(id=6)
                    ft_data = Cupos(cupos=pt, requerimiento=requirement)
                    ft_data.save()
                    ft_data.carrera.add(carrera)
                    ft_data.plan.add(plan)

                carreras_restantes -= 1
            #carrera_actual += 1
        return render(request, 'requerimientos/requerimientos-exito.html')
    else:
        print("wenaanannana")
        if not 'cupos' in request.session:
            return redirect('/requerimientos/')
        context = {}
        context['cupos'] = request.session['cupos']
        carreras = ["Ingenería Civil en Computación", "Ingeniería Civil Industrial",
                    "Ingeniería Civil, Mención Transportes",
                    "Ingeniería Civil, Mención Hidráulica, Sanitaria y Ambiental",
                    "Ingeniería Civil, Mención Estructuras y Construcción", "Ingeniería Civil en Química",
                    "Ingeniería Civil en Biotecnología", "Ingenería Civil Mecánica", "Ingeniería Civil Eléctrica",
                    "Ingeniería Civil Matemática", "Ingeniería Civil en Minas", "Geología"]
        context['carreras'] = carreras

        return render(request, 'requirements/cupos_por_carrera.html', context)  