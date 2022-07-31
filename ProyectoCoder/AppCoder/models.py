from codecs import unicode_escape_decode
from enum import unique
from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()
    class Meta():
        ordering = ('nombre', '-camada') # Ordena por curso asc. y por camada desc.
        unique_together = ('nombre', 'camada') # No permite que se repitan curso y camada

    #def __str__(self):
    #    return f'{self.nombre} - {self.camada}'
    # Muestra en la pagina del Admin "apellido, nombre"
   
class Estudiante(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    class Meta():
        ordering = ('apellido', 'nombre') # Ordena por appellido y nombre.
        unique_together = ('nombre', 'apellido', 'email') # No permite que se repitan.

    def __str__(self) -> str:
       return f'{self.apellido}, {self.nombre}'
    # Muestra en la pagina del Admin "apellido, nombre"

class Profesor(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    class Meta():
        ordering = ('apellido', 'nombre') # Ordena por apellido y nombre.
        unique_together = ('apellido', 'nombre', 'email', 'profesion') # No permite que se repitan.

    #def __str__(self) -> str:
    #    return f'{self.apellido}, {self.nombre} - {self.profesion}'
    # Muestra en la pagina del Admin "apellido, nombre - profesion"
class Entregable(models.Model):

    nombre = models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entregado = models.BooleanField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=1)
    # Clave Foranea. Vincula a otro Modelo. Relacion uno a muchos.
    # Un estudiante puede entregar varios entregables.
    # Un entregable puede ser entregado por un estudiante.
    # En estos casos se crea la clave foranea en el Modelo Secundario.

    def __str__(self) -> str:
        return f'{self.nombre} - {self.fechaDeEntrega}'
    # Muestra en la pagina del Admin "nombre - fechaDeEntrega"