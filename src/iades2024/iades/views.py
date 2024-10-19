from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from iades.models import Cursos, Estudiantes


def inicio(request):

    return render(request, "index.html")


def cursos(request):

    # Leer todos los objetos de una tabla
    cursos = Cursos.objects.all()    # select * from Cursos

    # Comandos del ORM
    # Filtrar por un campo
    cursos = Cursos.objects.filter(nombre="HTML")

    print(f"Curso filtrado: {cursos}")

    # Obtener un objeto unico -- un solo objeto
    cursos = Cursos.objects.get(id=2)

    print(f"Objeto unico {cursos.id}  {cursos.nombre}")

    context_cursos = {
        "cursos_list": cursos
    }

    return render(request, "cursos.html", context_cursos)


def estudiantes(request):

    # Trae todos los registros de la tabla estudiantes
    estudiantes = Estudiantes.objects.all()

    estudiantes = Estudiantes.objects.filter(dni=342422456)

    print(estudiantes)

    return HttpResponse("vista de estudiantes")


def profesores(request):

    return HttpResponse("vista de profesores")