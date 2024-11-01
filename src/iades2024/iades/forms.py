from django import forms


class FormularioCurso(forms.Form):

    nombre = forms.CharField()
    codigo = forms.IntegerField(max_value=100)


class FormularioBusquedaCurso(forms.Form):
    nombre = forms.CharField(max_length=10)
    codigo = forms.IntegerField(max_value=10)