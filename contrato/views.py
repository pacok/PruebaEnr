from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from contrato.forms import ContratoForm
from contrato.models import Contrato
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


# Create your views here.


def contrato(request):
	return HttpResponse("soy la pagina principal de contrato")


class ContratoList(ListView):
    model = Contrato
    template_name = 'contrato/contrato_list.html'

class ContratoCreate(CreateView):
	model = Contrato
	form_class = ContratoForm
	template_name = 'contrato/contrato_form.html'
	success_url = reverse_lazy('contrato:contrato_listar')

class ContratoUpdate(UpdateView):
	model = Contrato
	form_class = ContratoForm
	template_name = 'contrato/contrato_form.html'
	success_url = reverse_lazy('contrato:contrato_listar')

class ContratoDelete(DeleteView):
	model = Contrato
	template_name = 'contrato/contrato_delete.html'
	success_url = reverse_lazy('contrato:contrato_listar')