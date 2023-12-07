from django.contrib import admin
from .models import Asignatura
from .models import Alumno

admin.site.register(Asignatura)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'año_ingreso')
    list_filter = ('año_ingreso',)

admin.site.register(Alumno, AlumnoAdmin)

