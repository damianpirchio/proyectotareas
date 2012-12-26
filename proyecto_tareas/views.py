# -*- coding: utf-8 *-*
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.http import HttpResponseRedirect
#from django.http import Http404

from django.shortcuts import get_object_or_404

from django.template.response import TemplateResponse


def NuevoUsuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('index')
            return HttpResponseRedirect(url)
        else:
            form = UserCreationForm()
        return TemplateResponse(request, 'registration/register.html', {'form': form, })
