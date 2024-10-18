from django.contrib import admin

from .models import Cursos, Profesores, Estudiantes
# Register your models here.

admin.site.register(Cursos)
admin.site.register(Profesores)
admin.site.register(Estudiantes)