# proyecto-iades2024

Proyecto en Django IADES 2024

1. Creamos un entorno virtual

$ python -m venv <env_name>

2. Activamos el entorno virtual

# Linux

$ source <env_name>/bin/activate

# Windows

$ <env_name>\Scripts\activate.bat

3. Instalamos Django en el entorno

$ pip install django

4. [Opcional] Repositorio

5. Crear el proyecto

$ django-admin startproject <project_name>

<project_name>
<project_name>
manage.py

6. Creamos una app

$ python manage.py startapp <nombre_app>

<project_name>
<project_name>
manage.py
<nombre_app>
admin.py
apps.py
models.py
tests.py
views.py

7. Añadir la app en el archivo de configuracion del proyecto.(settings.py)

# Application definition

INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
"<nombre_app>",
]

8.  Generamos los modelos de nuestra app

# Django ORM

    class Cursos(models.Model):

        nombre = models.CharField(max_length=40)
        codigo = models.IntegerField()

9.  Corremos el comando makemigrations

$ python manage.py makemigrations

10. ver las migraciones

$ python manage.py showmigrations

11. para migrar

$ python manage.py migrate

Ayuda manage

$ python manage.py

Servidor de desarrollo

$ python manage.py runserver

1. Browser --> http://localhost:8000/<path_name>/

2. Entra en el servidor de desarrollo

3. urls.py

urlpatterns = [
path("admin/", admin.site.urls),
path("<path_name>/", view_name )
]

3. views.py

   def view_name():
   return HttpResponse(")

---

Bootstrap && CSS

1. Creamos adentro de la carpeta de la app una carpeta static

2. Vamos a https://startbootstrap.com/

3 Descargamos un template

4. Descomprimimos el archivo
