from django.db import models

# Create your models here.


class Cursos(models.Model):

    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField()

    def __str__(self):
        return f"curso: {self.nombre} -- codigo: {self.codigo}"


class Estudiantes(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.CharField(max_length=8, unique=True, blank=True, null=False)

    def __str__(self):
        return f"Estudiantes -- nombre: {self.nombre} -- dni: {self.dni}"
