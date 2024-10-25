from django import forms


class FormularioCurso(forms.Form):

    nombre = forms.CharField()
    codigo = forms.IntegerField()