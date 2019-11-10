from django import forms
from .models import Requerimiento
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Field, Row, Column, Fieldset, HTML


class RequirementForm(forms.ModelForm):

    productora_nombre = forms.CharField(max_length=50, label="Nombre productora", required=False)
    persona_nombre = forms.CharField(max_length=50, label="Persona de contacto de la productora", required=False)
    productora_contacto = forms.CharField(max_length=50, label="Teléfono de la persona de contacto", required=False)
    productora_email = forms.CharField(max_length=50, label="Teléfono de la persona de contacto", required=False)

    class Meta:
        model = Requerimiento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RequirementForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-req-form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = '/requerimientos/'
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
            HTML("<fieldset><legend hidden id='producer_legend'>Datos de la productora que instalará su stand propio.</legend>"),
            Div('productora_nombre', css_class ='col-md-6', id="div-prod-nombre", style="display: none;"),
            Div('persona_nombre', css_class ='col-md-6', id="div-pers-nombre", style="display: none;"),
            Div('productora_contacto', css_class ='col-md-6', id="div-con-nombre", style="display: none;"),
            Div('productora_email', css_class ='col-md-6', id="div-email-nombre", style="display: none;"),
            HTML("</fieldset>"),
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

        )

        #self.helper.add_input(Submit('submit', 'Submit'))

    def clean(self):
        cleaned_data = super(RequirementForm, self).clean()
        entrevistadores = cleaned_data.get('entrevistadores')
        tipo_stand = cleaned_data.get('tipo_stand')
        stand1 = cleaned_data.get('stand1')
        stand2 = cleaned_data.get('stand2')
        stand3 = cleaned_data.get('stand3')
        almuerzos_normales = cleaned_data.get('almuerzos_normales')
        almuerzos_vegetarianos = cleaned_data.get('almuerzos_vegetarianos')
        almuerzos = almuerzos_normales + almuerzos_vegetarianos
        if entrevistadores:
            if tipo_stand == '1' and (entrevistadores > 2 or entrevistadores <= 1):
                raise forms.ValidationError(
                    "El Stand Simple sólo se admite un máximo de 2 entrevistadores."
                )
            elif tipo_stand == '2' and (entrevistadores > 3 or entrevistadores <= 1):
                raise forms.ValidationError(
                    "El Stand Especial 4 sólo se admite un máximo de 3 entrevistadores."
                )
            elif tipo_stand == '3' and (entrevistadores > 4 or entrevistadores <= 1):
                raise forms.ValidationError(
                    "El Stand Especial 5 sólo se admite un máximo de 4 entrevistadores."
                )
            elif tipo_stand == '4' and (entrevistadores > 4 or entrevistadores <= 1):
                raise forms.ValidationError(
                    "El Stand Doble sólo se admite un máximo de 4 entrevistadores."
                )
        if almuerzos:
            if tipo_stand == '1' and almuerzos > 2:
                raise forms.ValidationError(
                    "El Stand Simple sólo se admite un máximo de 2 almuerzos."
                )
            elif tipo_stand == '2' and almuerzos > 3:
                raise forms.ValidationError(
                    "El Stand Especial 4 sólo se admite un máximo de 3 almuerzos."
                )
            elif tipo_stand == '3' and almuerzos > 4:
                raise forms.ValidationError(
                    "El Stand Especial 5 sólo se admite un máximo de 4 almuerzos."
                )
            elif tipo_stand == '4' and almuerzos > 4:
                raise forms.ValidationError(
                    "El Stand Doble sólo se admite un máximo de 4 almuerzos."
                )
            elif almuerzos < 0:
                raise forms.ValidationError(
                    "El número de almuerzos debe ser un número mayor a cero."
                )
        if stand1 and stand2 and stand3:
            if stand1 == stand2:
                raise forms.ValidationError(
                    "Sus preferencias de Stand deben ser distintas."
                )
            elif stand2 == stand3:
                raise forms.ValidationError(
                    "Sus preferencias de Stand deben ser distintas."
                )
            elif stand1 == stand3:
                raise forms.ValidationError(
                    "Sus preferencias de Stand deben ser distintas."
                )
            elif stand1 == stand2 == stand3:
                raise forms.ValidationError(
                    "Sus preferencias de Stand deben ser distintas."
                )