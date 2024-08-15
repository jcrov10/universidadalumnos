from django import forms
from .models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'matricula', 'fecha_nacimiento', 'email', 'telefono']
