# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.functions import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from licitacion.forms import LicitacionForm
from licitacion.models import Licitacion
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


# Create your views here.

def licitacion(request):
    return render(request, 'licitacion/index.html')


def licitacion_view(request):
    if request.method == 'POST':
        form = LicitacionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('licitacion:index')
    else:
        form = LicitacionForm()
    return render(request, 'licitacion/licitacion_form.html', {'form': form})


def licitacion_list(request):
    licitacion = Licitacion.objects.all().order_by('id')
    contexto = {'licitaciones': licitacion}
    return render(request, 'licitacion/licitacion_list.html', contexto)


class LicitacionList(ListView):
    model = Licitacion
    template_name = 'licitacion/licitacion_list.html'


class LicitacionCreate(CreateView):
    model = Licitacion
    form_class = LicitacionForm
    template_name = 'licitacion/licitacion_form.html'
    success_url = reverse_lazy('licitacion:licitacion_listar')


class LicitacionUpdate(UpdateView):
    model = Licitacion
    form_class = LicitacionForm
    template_name = 'licitacion/licitacion_form.html'
    success_url = reverse_lazy('licitacion:licitacion_listar')


class LicitacionDelete(DeleteView):
    model = Licitacion
    template_name = 'licitacion/licitacion_delete.html'
    success_url = reverse_lazy('licitacion:licitacion_listar')


