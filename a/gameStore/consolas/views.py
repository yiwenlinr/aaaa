from django.shortcuts import render
from consolas.forms import FormProyecto
from consolas.models import Proyecto
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'consolas/index.html')

def listadoProyectos(request):
    proyectos = Proyecto.objects.all()
    data = {'proyectos': proyectos}
    return render(request, 'consolas/proyectos.html', data)

def agregarProyecto(request):
    form = FormProyecto()
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    data = {'form': form}
    return render(request, 'consolas/agregarProyecto.html', data)

def eliminarProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    proyecto.delete()
    return HttpResponseRedirect('/proyectos')

def actualizarProyecto(request, id):
    proyecto = Proyecto.objects.get(id = id)
    form = FormProyecto(instance=proyecto)
    if request.method == 'POST':
        form = FormProyecto(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'consolas/agregarProyecto.html', data)