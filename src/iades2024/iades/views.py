from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
from iades.models import Curso, Estudiante, Profesor
from iades.forms import FormularioCurso, FormularioBusquedaCurso, FormularioProfesor

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
    cursos = Curso.objects.all()    # select * from Cursos
    print(cursos)

    # Comandos del ORM
    # Filtrar por un campo
    cursos_html = Curso.objects.filter()
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
    estudiantes = Estudiante.objects.all()

    estudiantes = Estudiante.objects.filter(dni=342422456)

    print(estudiantes)

    return HttpResponse("vista de estudiantes")


def profesores(request):

    # vamos a dar de alta un profesor en esta vista
    if request.method == "POST":
        
        profesor_form = FormularioProfesor(request.POST)

        if profesor_form.is_valid():

            datos_profesor = profesor_form.cleaned_data

            profesor_new = Profesor(**datos_profesor)

            profesor_new.save()

            return render(request, "index.html")

    profesor_form = FormularioProfesor()
    return render(request, "profesores.html", {"profesor": profesor_form})
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
            curso_new = Curso(nombre=datos["nombre"], codigo=datos["codigo"])
            curso_new.save()
            return HttpResponseRedirect("/instituto/")
        
        else:
            # print(f"errores: {formulario.errors}")
            print(f"errores json: {formulario.errors.as_json}")
            print(f"errores data: {formulario.errors.as_data}")
            print(f"errores text: {formulario.errors.as_text}")
            return render(request, "formulario_curso.html", {"formulario": formulario})
        
    formulario = FormularioCurso({"nombre": "SCRUM", "codigo": 4})
    return render(request, "formulario_curso.html", {"formulario": formulario})
    # return render(request, "formulario_curso.html")


def buscar_curso(request):

    formulario = FormularioBusquedaCurso()

    return render(request, "buscar_curso.html", {"formulario": formulario})


def buscar_nombre_curso(request):

    parametros_url_nombre = request.GET["nombre"]

    print(f"url parametros: {parametros_url_nombre}")

    # curso_nombre = Curso.objects.filter(nombre=parametros_url_nombre)
    curso_nombre = Curso.objects.filter(nombre__icontains=parametros_url_nombre)

    print(curso_nombre)

    return render(request, "listado_busqueda_cursos.html", {"id": "pirulo", "cursos" : curso_nombre, "nombre" : parametros_url_nombre})


def listar_profesores(request):

    profesores = Profesor.objects.all()

    # TODO contar cantidad 
    cantidad = Profesor.objects.count()

    context_profesores = { "profesores": profesores, "cantidad": cantidad}

    return render(request, 'listar_profesores.html', context_profesores)


def eliminar_profesor(request, prof_dni):

    print(prof_dni)

    return HttpResponse("Vista en construccion")


def iniciar_sesion(request):

    if request.method == "POST":
        
        formulario = AuthenticationForm(request, data=request.POST)
        print(f"formulario: {formulario}")
        if formulario.is_valid():

            print("Form is valid")

            usuario = formulario.cleaned_data.get("username")
            password = formulario.cleaned_data.get("password")

            user = authenticate(username=usuario, password=password)

            print(f"user: {user}")

            if user is not None:

                login(request, user)

                print(f"Bienvenido: {usuario}")

                return render(request, "index.html")    
            
        else:
            print("Error")
            print(f"errores: {formulario.errors}")

    formulario = AuthenticationForm()

    return render(request, 'login.html', {"form": formulario})

""""
def registracion(request):

    if request.methos == "POST":

        # Registramos el usuario

    
    formulario = 

"""