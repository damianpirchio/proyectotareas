# -*- coding: utf-8-*-

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'proyecto_tareas.views.home', name='home'),
    #url(r'^proyecto_tareas/', include('proyecto_tareas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # aquí incluimos las urls definidas por la app tareasapp
    url(r'^tareasapp/', include('tareasapp.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
    name='logout'),
    #url(r'^register/$', 'tareasapp.views.NuevoUsuario', name='NuevoUsuario'),
    url(r'^register/$', 'proyecto_tareas.views.NuevoUsuario', name='NuevoUsuario'),
)
