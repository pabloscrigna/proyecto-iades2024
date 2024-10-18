from django.urls import path

from .views import cursos, estudiantes, profesores, inicio


urlpatterns = [
    path("", inicio, name="Inicio"),
    path("cursos/", cursos, name="Cursos"),
    path("estudiantes/", estudiantes, name="Estudiantes"),
    path("profesores/", profesores, name="Profesores"),
]