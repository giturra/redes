from django import forms
from .models import Perfil
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Field, Submit


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'carrera', 'empleo', 'foto_perfil', 'cv',
            'ano_ingreso', 'ano_egreso', 'perfil_pro'
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-profile-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = '/perfil/'

        self.helper.layout = Layout(
            Field('carrera'),
            Field('empleo'),
            Field('foto_perfil'),
            Field('cv'),
            Field('ano_ingreso'),
            Field('ano_egreso'),
            Field('perfil_pro'),
        )