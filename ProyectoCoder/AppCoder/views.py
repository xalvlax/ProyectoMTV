from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from AppCoder.models import Curso

# Create your views here.

def curso(request, nombre, camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    documento = f'>>>>> Se agrego Curso: {curso.nombre} - Camada: {curso.camada} <<<<<'

    return HttpResponse(documento)

def lista_curso(request):

    lista = Curso.objects.all()
    diccionario = {'lista_cursos': lista}
    plantilla = loader.get_template('lista_cursos.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def inicio (request):

    return render(request, 'inicio.html')

def cursos (request):

    return render(request, 'cursos.html')

def profesores (request):

    return render(request, 'profesores.html')

def estudiantes (request):

    return render(request, 'estudiantes.html')

def entregables (request):

    return render(request, 'entregables.html')

