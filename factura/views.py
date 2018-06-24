# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from factura.models import Factura
from factura.forms import FacturaForm
# Create your views here.

def factura(request):
    return HttpResponse("Estoy en factura")

class FacturaList(ListView):
    model = Factura
    template_name = 'factura/factura_list.html'


class FacturaCreate(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'factura/factura_form.html'
    success_url = reverse_lazy('factura:factura_listar')


class FacturaUpdate(UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'factura/factura_form.html'
    success_url = reverse_lazy('factura:factura_listar')


class FacturaDelete(DeleteView):
    model = Factura
    template_name = 'factura/factura_delete.html'
    success_url = reverse_lazy('factura:factura_listar')

