from django.urls import path

from .views import cursos, estudiantes, profesores, inicio, formulario_curso


urlpatterns = [
    path("", inicio, name="Inicio"),
    path("cursos/", cursos, name="Cursos"),
    path("estudiantes/", estudiantes, name="Estudiantes"),
    path("profesores/", profesores, name="Profesores"),
    path('curso-nuevo/', formulario_curso, name="FormularioCurso" )
]