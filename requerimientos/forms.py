from django import forms
from .models import Requerimiento
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Field, Row, Column, Fieldset


class RequirementForm(forms.ModelForm):
    class Meta:
        model = Requerimiento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RequirementForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(

            Field('nombre_empresa', css_class='form_control'),
            Div(Field('descripcion', css_class='form_control'), css_class='textarea_requerimientos'),
            Field('representante'),
            Field('celular'),
            Field('email'),
            Fieldset('Día de Asistencia', Div('dia_asistencia')),
            Fieldset('Tipo de Stand',
                     Div('tipo_stand', css_class='col-md-6'),
                     Div('stand_propio', css_class='col-md-6')
            ),
            Fieldset('Preferencia de Stand Layout',
                     Div('stand1', css_class='col-md-4'),
                     Div('stand2', css_class='col-md-4'),
                     Div('stand3', css_class='col-md-4')
            ),
            Fieldset('Cantidad de Almuerzos',
                     Div('entrevistadores', css_class='col-md-4'),
                     Div('almuerzos_normales', css_class='col-md-4'),
                     Div('almuerzos_vegetarianos', css_class='col-md-4')
                     ),
            Fieldset('Detalle de Entrevista',
                     Div('tipo_entrevista', css_class='col-md-6'),
                     Div('tiempo_entrevista', css_class='col-md-6')
                     ),
            Div('formato_entrevista', css_class='col-md-12'),
            Submit('submit', 'Submit')

        )

        #self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super(RequirementForm, self).clean()
        nombre = cleaned_data.get('nombre_empresa')
