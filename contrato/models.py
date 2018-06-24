# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from licitacion.models import Licitacion


# Create your models here.
class Contrato(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField()
    licitacion = models.ForeignKey(Licitacion, null=True, blank=True, on_delete=models.CASCADE)



