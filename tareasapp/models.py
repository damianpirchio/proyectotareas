from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=64)
    descripcion = models.CharField(default="", max_length=64)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categorias'

    def __unicode__(self):
        return self.nombre


class Tarea(models.Model):

    TIPOS_DE_ESTADO = (
        (u'P', u'Pendiente'),
        (u'X', u'Cancelado'),
        (u'C', u'Completado'),
        )

    slug = models.SlugField(unique=True)
    titulo = models.CharField(max_length=64)
    descripcion = models.TextField()
    estado = models.CharField(max_length=1, default=u'P', choices=TIPOS_DE_ESTADO)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_limite = models.DateField(null=False, blank=False)
    fecha_realizacion = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True)
    usuario = models.ForeignKey(User)

    #class Meta:
        #ordering = ['-fecha_creacion']

    def __unicode__(self):
        return self.titulo
