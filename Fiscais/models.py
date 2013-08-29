# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from concursos.models import Concurso

class Prova(models.Model):
    descricao = models.CharField(max_length=30) 
    concurso = models.ForeignKey(Concurso)
    
    def __unicode__(self):
        return '%s (%s) ' % (self.descricao, self.concurso)

class Sala(models.Model):
    local = models.CharField(max_length=30)
    predio = models.CharField(max_length=30)
    prova = models.ForeignKey(Prova)
    numero = models.IntegerField()

    def __unicode__(self):
        return 'Sala %s (%s) ' % (self.numero, self.predio)
    
class Fiscal(models.Model):
    salas = models.ManyToManyField(Sala)
    usuario = models.OneToOneField(User)
    def __unicode__(self):
        return self.usuario.username
    