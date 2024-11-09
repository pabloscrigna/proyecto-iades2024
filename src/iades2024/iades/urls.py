from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (cursos,
                    estudiantes,
                    profesores,
                    inicio,
                    formulario_curso,
                    buscar_curso,
                    buscar_nombre_curso,
                    listar_profesores,
                    eliminar_profesor,
                    iniciar_sesion,
                    registracion,
)


urlpatterns = [
    path("", inicio, name="Inicio"),
    path("cursos/", cursos, name="Cursos"),
    path("estudiantes/", estudiantes, name="Estudiantes"),
    path("profesores/", profesores, name="Profesores"),
    path('curso-nuevo/', formulario_curso, name="FormularioCurso"),
    path('buscar-curso/', buscar_curso, name="BuscarCurso"),
    path('buscar-nombre-curso', buscar_nombre_curso, name="BuscarNombreCurso"),
    path('listar-profesores/', listar_profesores, name="listarProfesores"),
    path('eliminar-profesor/<prof_dni>/', eliminar_profesor, name="EliminarProfesor"),
    path('login/', iniciar_sesion, name="Login"),
    path('logout', LogoutView.as_view(template_name='logout_termplate.html'), name="Logout"),
    path('registracion/', registracion, name="Registracion")
]