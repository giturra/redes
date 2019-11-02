from django import forms
from .models import Requerimiento
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Field, Row, Column, BaseInput, Fieldset


class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requerimiento
        fields = ['nombre_empresa', 'descripcion', 'representante', 'celular', 'email']

    def __init__(self, *args, **kwargs):
        super(RequirementForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(

            Field('nombre_empresa'),
            Field('descripcion'),
            Field('representante'),
            Field('celular'),
            Field('email'),
            Fieldset('Día de Asistencia', Div('dahjdhj'))

        )

        #self.helper.add_input(Submit('submit', 'Submit'))