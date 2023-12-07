from django import forms
from .models import Alumno

class AlumnoFilterForm(forms.Form):
    año_ingreso = forms.MultipleChoiceField(choices=[], required=False)

    def __init__(self, *args, **kwargs):
        super(AlumnoFilterForm, self).__init__(*args, **kwargs)
        años_disponibles = Alumno.objects.values_list('año_ingreso', flat=True).distinct()
        años_disponibles = [(año, año) for año in años_disponibles if año is not None]
        self.fields['año_ingreso'].choices = años_disponibles