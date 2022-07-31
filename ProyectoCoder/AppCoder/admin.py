from django.contrib import admin
from AppCoder.models import Curso, Entregable, Estudiante, Profesor
# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'camada'] # Muestra en tablas
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['apellido', 'nombre', 'email', 'profesion'] # Muestra en tablas
    search_fields = ['nombre', 'apellido'] # Buscador por nombre o apellido

admin.site.register(Curso, CursoAdmin)

admin.site.register(Profesor, ProfesorAdmin)

admin.site.register(Estudiante)

admin.site.register(Entregable)
