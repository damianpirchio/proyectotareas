# -*- coding: utf-8 *-*

from django.conf.urls import patterns, include, url


urlpatterns = patterns('tareasapp.views',
    #url(r'^testing/$', 'testing'),
    #url(r'^(?P<post_id>\d+)/$', 'post_detail', name='post-detail'),
    #url(r'^new-post/$', 'new_post', name='new-post'),
    url(r'^$', 'index', name='index'),
    url(r'^newtask/$', 'NuevaTarea', name='NuevaTarea'),
    url(r'^tasklist/$', 'ListaTareas', name='ListaTareas'),
)
