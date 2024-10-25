from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from iades.models import Cursos, Estudiantes
from iades.forms import FormularioCurso

def inicio(request):

    return render(request, "index.html")


def cursos(request):

    print(f"metodo: {request.method}")  # GET    # POST - GET - PUT - PATCH 

    # Crea un curso por unica vez
    # nombre --> str y codigo --> int

    # curso_new = Cursos(nombre="tiene 5 para pensar", codigo=34125)
    # print(curso_new)

    # curso_new.save()

    # print(f"id= {curso_new.id}")

    # Leer todos los objetos de una tabla
    cursos = Cursos.objects.all()    # select * from Cursos
    print(cursos)

    # Comandos del ORM
    # Filtrar por un campo
    cursos_html = Cursos.objects.filter()
    cursos_html = cursos_html.first()
    print(f"Curso filtrado: {cursos_html}")

    # Obtener un objeto unico -- un solo objeto
    #cursos_id = Cursos.objects.get(id=6)
    #print(type(cursos_id))
    #print(f"Objeto unico: id: {cursos_id.id} -- nombre: {cursos_id.nombre}")

    #cursos_id.nombre = "Rust"
    #cursos_id.save()

    context_cursos = {
        "cursos_list": cursos,
        #"curso_id": cursos_id   # id = 6 nombre Rust codigo 45634
    }

    # elimina un curso 
    # cursos_id.delete()    # Borra de la base y el el id de la variable = None nombre = Rust codigo 45634

    return render(request, "cursos.html", context_cursos)


def estudiantes(request):

    # Trae todos los registros de la tabla estudiantes
    estudiantes = Estudiantes.objects.all()

    estudiantes = Estudiantes.objects.filter(dni=342422456)

    print(estudiantes)

    return HttpResponse("vista de estudiantes")


def profesores(request):

    return render(request, "profesores.html")
    #return HttpResponse("vista de profesores")


def formulario_curso(request):

    if request.method == "POST":

        formulario = FormularioCurso(request.POST)

        print("formulario")
        print(formulario)

        print(f" validadcion: {formulario.is_valid()}")

        if formulario.is_valid():
            datos = formulario.cleaned_data
            print(f"datos: {datos}")
            curso_new = Cursos(nombre=datos["nombre"], codigo=datos["codigo"])
            curso_new.save()

        else:
            print(f"errores: {formulario.errors}")

        return render(request, "index.html")

    return render(request, "formulario_curso.html")