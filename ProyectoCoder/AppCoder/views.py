from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from AppCoder.models import Curso

# Create your views here.

def curso(self, nombre, camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    documento = f'>>>>> Se agrego Curso: {curso.nombre} - Camada: {curso.camada} <<<<<'

    return HttpResponse(documento)

def lista_curso(self):

    lista = Curso.objects.all()
    diccionario = {'lista_cursos': lista}
    plantilla = loader.get_template('lista_cursos.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def inicio (self):

    return render(self, 'inicio.html')

def cursos (self):

    return render(self, 'cursos.html')

def profesores (self):

    return render(self, 'profesores.html')

def estudiantes (self):

    return render(self, 'estudiantes.html')

def entregables (self):

    return render(self, 'entregables.html')
