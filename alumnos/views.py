from django.shortcuts import render, get_object_or_404, redirect
from .models import Alumno
from .forms import AlumnoForm

# Vista para la página de Inicio
def inicio(request):
    return render(request, 'alumnos/inicio.html')

# Vista para Listar Estudiantes
def lista_estudiantes(request):
    estudiantes = Alumno.objects.all()
    return render(request, 'alumnos/lista_estudiantes.html', {'estudiantes': estudiantes})

# Vista para Insertar un Nuevo Estudiante
def registrar_estudiante(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos/registrar_estudiante.html', {'form': form})

# Vista para Editar un Estudiante Existente
def editar_estudiante(request, id):
    estudiante = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = AlumnoForm(instance=estudiante)
    return render(request, 'alumnos/editar_estudiante.html', {'form': form})

# Vista para Eliminar un Estudiante
def eliminar_estudiante(request, id):
    estudiante = get_object_or_404(Alumno, id=id)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('lista_estudiantes')
    return render(request, 'alumnos/eliminar_estudiante.html', {'estudiante': estudiante})

# Vista para la página de Contacto
def contacto(request):
    return render(request, 'contacto.html')
