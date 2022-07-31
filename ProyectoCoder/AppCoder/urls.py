from django.urls import path
from AppCoder.views import curso, lista_curso
from AppCoder.views import cursos, entregables, estudiantes, inicio, profesores

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>/', curso),
    path('lista-cursos/', lista_curso),
    path('', inicio, name='Inicio'),
    path('cursos/', cursos, name='Cursos'),
    path('profesores/', profesores, name='Profesores'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables, name='Entregables'),
]
