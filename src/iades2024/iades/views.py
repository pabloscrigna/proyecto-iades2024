from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def inicio(request):

    return render(request, "index.html")


def cursos(request):

    context_cursos = {
        "id" : 45,
        "nombre" : "python",
        "alumnos" : 45
    }

    return render(request, "cursos.html", context_cursos)


def estudiantes(request):

    return HttpResponse("vista de estudiantes")


def profesores(request):

    return HttpResponse("vista de profesores")