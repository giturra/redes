from django import forms
from .models import Perfil
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Field


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['rut', 'carrera', 'empleo']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-profile-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        # self.helper.layout = Layout(
        #     Field('usuario.firstname', css_class='form_control'),
        # )