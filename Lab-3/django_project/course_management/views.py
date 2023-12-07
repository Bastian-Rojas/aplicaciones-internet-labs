from django.shortcuts import render
from .models import Alumno
from .models import Asignatura
from .forms import AlumnoFilterForm

def lista_asignaturas(request):
    asignaturas = Asignatura.objects.all()
    
    return render(request, 'lista_asignaturas.html', {'asignaturas': asignaturas})

def crear_asignatura(request):
    return render(request, 'crear_asignatura.html')

def detalle_asignatura(request):
    asignaturas = Asignatura.objects.all()
    return render(request, 'detalle_asignatura.html', {'asignaturas': asignaturas})

def crear_alumno(request):
    return render(request, 'crear_alumno.html')

def lista_alumno(request):
    alumnos = Alumno.objects.all()
    return render(request, 'lista_alumno.html', {'alumnos': alumnos})

from django.shortcuts import render
from .models import Asignatura

from django.shortcuts import render

def buscar_asignatura(request):
    return render(request, 'buscar_asignatura.html')

def resultado_busqueda(request):
    filtro = request.GET.get('filtro', '')
    asignaturas = Asignatura.objects.filter(nombre__icontains=filtro) if filtro else []
    return render(request, 'resultado_busqueda.html', {'asignaturas': asignaturas})

def lista_alumnos(request):
    form = AlumnoFilterForm(request.GET or None)
    alumnos = Alumno.objects.all()

    if form.is_valid():
        años_ingreso = form.cleaned_data.get('año_ingreso')
        if años_ingreso:
            alumnos = alumnos.filter(año_ingreso__in=años_ingreso)

    return render(request, 'lista_alumno.html', {'form': form, 'alumnos': alumnos})
    


    
