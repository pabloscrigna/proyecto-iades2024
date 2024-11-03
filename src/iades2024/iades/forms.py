from django import forms


class FormularioCurso(forms.Form):

    nombre = forms.CharField()
    codigo = forms.IntegerField(max_value=100)


class FormularioBusquedaCurso(forms.Form):
    nombre = forms.CharField(max_length=10)
    codigo = forms.IntegerField(max_value=10)


class FormularioProfesor(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    dni = forms.CharField(max_length=8)
    legajo = forms.IntegerField()
