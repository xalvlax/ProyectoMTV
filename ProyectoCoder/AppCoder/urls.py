from django.urls import path
from AppCoder.views import curso, lista_curso
from AppCoder.views import cursos, entregables, estudiantes, inicio, profesores

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>/', curso),
    path('lista-cursos/', lista_curso),
    path('', inicio),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
]
