# -*- coding: utf-8 *-*

from django.conf.urls import patterns, include, url


urlpatterns = patterns('tareasapp.views',
    #url(r'^testing/$', 'testing'),
    url(r'^(?P<tarea_id>\d+)/$', 'DetalleTarea', name='DetalleTarea'),
    url(r'^borrar-tarea/(?P<tarea_id>\d+)/$', 'BorrarTarea',
        name='BorrarTarea'),
    url(r'^editar-tarea/(?P<tarea_id>\d+)/$', 'EditarTarea',
        name='EditarTarea'),
    url(r'^filtrar-categoria/(?P<categoria_id>\d+)/$', 'FiltrarCategoria',
        name='FiltrarCategoria'),
    url(r'^$', 'index', name='index'),
    url(r'^newtask/$', 'NuevaTarea', name='NuevaTarea'),
    url(r'^newcategory/$', 'NuevaCategoria', name='NuevaCategoria'),
    url(r'^tasklist/$', 'ListaTareas', name='ListaTareas'),
)
