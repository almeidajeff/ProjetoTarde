# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from concursos.models import Concurso

class Prova(models.Model):
    concurso = models.ForeignKey(Concurso)

class Sala(models.Model):
    local = models.CharField(max_length=30)
    predio = models.CharField(max_length=30)
    prova = models.ForeignKey(Concurso)
    numero = models.IntegerField()

class Fiscal(models.Model):
    salas = models.ManyToManyField(Sala)
    usuario = models.OneToOneField(User)
