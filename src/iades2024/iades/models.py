from django.db import models

# Create your models here.


""""
class ProductoBase(models.Model):
    # form que viene desde el front 
    descripcion =
    precio 
    color 
    descuento (default = 0)

    class Meta:
     abstract = True

class Producto(ProductoBase):

    creado =
    actualizado =
    precio_descuento = 

"""

class DatosBase(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.CharField(max_length=8, unique=True, blank=False, null=False)

    class Meta:
        abstract = True


class Oyente(DatosBase):
    
    curso = models.IntegerField()


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    codigo = models.IntegerField()
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f"curso: {self.nombre} -- codigo: {self.codigo}"


class Estudiante(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.CharField(max_length=8, unique=True, blank=True, null=False)

    def __str__(self):
        return f"Estudiantes -- nombre: {self.nombre} -- dni: {self.dni}"


class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.CharField(max_length=8, unique=True, blank=False, null=False)
    legajo = models.IntegerField()
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profesor -- nombre: {self.nombre} -- dni: {self.dni}"

    class Meta:
        verbose_name_plural = 'Profesores'