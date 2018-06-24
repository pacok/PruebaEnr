# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from licitacion.models import Licitacion
from contrato.models import Contrato


class Factura(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField(auto_now_add=True)
    adjunto = models.FileField(upload_to="media/")
    checkbox = models.BooleanField(default=True)
    licitacion = models.ForeignKey(Licitacion, on_delete=models.CASCADE)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    iva = models.DecimalField(max_digits=8,decimal_places=2)
    total = models.DecimalField(max_digits=8,decimal_places=2)


