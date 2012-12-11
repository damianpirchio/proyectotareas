# -*- coding: utf-8 -*-

from django.contrib import admin

from tareasapp.models import Tarea, Categoria


class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}


class TareaAdmin(admin.ModelAdmin):
    #date_hierarchy = 'publish_on'
    prepopulated_fields = {'slug': ('titulo',)}
    #list_display = ('title', 'category', 'publish_on')
    #list_filter = ('publish_on', 'category', 'authors')
    fieldsets = (
        (None, {
            'fields': ('titulo', 'slug', 'descripcion',
                        'fecha_limite', 'usuario', 'categoria',),
        }),
        #('Metadata', {
            #'fields': ('fecha_creacion', 'usuario', 'categoria',),
        #})
    )


admin.site.register(Tarea, TareaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
