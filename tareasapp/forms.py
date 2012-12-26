# -*- coding: utf-8 *-*

from django.forms import ModelForm

from tareasapp.models import Tarea

#from django.forms.widgets import SplitDateTimeWidget
from django.forms.extras.widgets import SelectDateWidget

class TareaForm(ModelForm):

    class Meta:

        model = Tarea
        widgets = {
                    'fecha_limite': SelectDateWidget(),
                    #'fecha_limite': SplitDateTimeWidget(),
                  }
        exclude = (
                    "fecha_creacion",
                    "fecha_realizacion",
                    "estado",
                 )
