# -*- coding: utf-8 *-*

from django.conf.urls import patterns, include, url


urlpatterns = patterns('tareasapp.views',
    #url(r'^testing/$', 'testing'),
    url(r'^(?P<tarea_id>\d+)/$', 'DetalleTarea', name='DetalleTarea'),
    url(r'^borrar-tarea/(?P<tarea_id>\d+)/$', 'BorrarTarea', name='BorrarTarea'),
    #url(r'^new-post/$', 'new_post', name='new-post'),
    url(r'^$', 'index', name='index'),
    url(r'^newtask/$', 'NuevaTarea', name='NuevaTarea'),
    url(r'^newcategory/$', 'NuevaCategoria', name='NuevaCategoria'),
    url(r'^tasklist/$', 'ListaTareas', name='ListaTareas'),
)
