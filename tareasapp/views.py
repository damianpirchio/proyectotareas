# Create your views here.

from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from django.http import Http404

from django.shortcuts import get_object_or_404

from django.template.response import TemplateResponse

from tareasapp.forms import TareaForm, EditarTareaForm, CategoriaForm
from tareasapp.models import Tarea, Categoria
from django.template import defaultfilters
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    """View para mostrar el menu del usuario"""
    #post = get_object_or_404(Post, id=post_id)

    return TemplateResponse(
        request, 'tareasapp/index.html',)


def NuevaTarea(request):
    #if not request.user.is_authenticated():
        #raise Http404
    if request.method == 'POST':
        # Procesamos el form
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.slug = defaultfilters.slugify(tarea.titulo)
            tarea.estado = u'P'
            tarea.fecha_realizacion = None
            tarea.fecha_creacion = timezone.now()
            tarea.usuario = request.user
            tarea.save()
            url = reverse('ListaTareas', )
            return HttpResponseRedirect(url)
    else:
        form = TareaForm()
    return TemplateResponse(request, 'tareasapp/newtask.html', {'form': form, })


def NuevaCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.slug = defaultfilters.slugify(categoria.nombre)
            categoria.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = CategoriaForm()
    return TemplateResponse(request, 'tareasapp/newcategory.html', {'form': form, })


def ListaTareas(request):
    tareas = Tarea.objects.filter(usuario=request.user).order_by('fecha_limite')
    categorias = Categoria.objects.all()
    return TemplateResponse(request, 'tareasapp/tasklist.html', {'tareas': tareas, 'categorias': categorias, })


def FiltrarCategoria(request):
    datos = request.GET
    cat_id = datos.get('categoria_id')
    try:
        user = request.user
        if (cat_id == '-1'):
            category = Categoria.objects.all()
            categorias = Categoria.objects.all()
            tareas = Tarea.objects.filter(usuario=user,
            categoria=category).order_by('fecha_limite')
        else:
            category = Categoria.objects.filter(id=cat_id)
            categorias = Categoria.objects.all()
            tareas = Tarea.objects.filter(usuario=user,
            categoria=category).order_by('fecha_limite')
    except tareas.DoesNotExist:
            return TemplateResponse(request, 'tareasapp/tasklist.html', {'tareas': tareas, 'categorias': categorias})
    return TemplateResponse(request, 'tareasapp/tasklist.html', {'tareas': tareas, 'categorias': categorias})

def DetalleTarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    return TemplateResponse(request, 'tareasapp/taskdetail.html', {'tarea': tarea, })


def BorrarTarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect("ListaTareas")


def EditarTarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    if request.method == 'POST':
        form = EditarTareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ListaTareas'))
    else:
        form = EditarTareaForm(instance=tarea)
    return TemplateResponse(request,
             'tareasapp/edittask.html', {'form': form, })
