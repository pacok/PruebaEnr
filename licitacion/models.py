# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Licitacion(models.Model):
    nombre = models.CharField(max_length=50)
    publicada = models.BooleanField(default=True)


def __str__(self):
    return self.nombre
