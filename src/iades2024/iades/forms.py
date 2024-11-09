from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class RegistracionUsuario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password1 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = { k: "" for k in fields} 