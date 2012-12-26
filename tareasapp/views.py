# Create your views here.

from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from django.http import Http404

from django.shortcuts import get_object_or_404

from django.template.response import TemplateResponse

from tareasapp.forms import TareaForm
from tareasapp.models import Tarea
from django.template import defaultfilters
from django.utils import timezone


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
        #form = TareaForm(initial={'usuario': 'Alguien'})
        form = TareaForm()
    return TemplateResponse(request, 'tareasapp/newtask.html', {'form': form, })


def ListaTareas(request):
    tareas = Tarea.objects.all().order_by('titulo')
    return TemplateResponse(request, 'tareasapp/tasklist.html', {'tareas': tareas, })


