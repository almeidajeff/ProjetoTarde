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
    prova = models.ForeignKey(Prova)
    numero = models.IntegerField()
    
    def __unicode__(self):
        """ Mostrar o nome do objeto """
        return '%s' %(self.predio)
        
    class Admin (admin.ModelAdmin):
        list_display = ('predio',)

class Fiscal(models.Model):
    salas = models.ManyToManyField(Sala)
    usuario = models.OneToOneField(User)

    def __unicode__(self):
        """ Mostrar o nome do objeto """
        return '%s %s' %(self.usuarios,self.salas)
        
    class Admin (admin.ModelAdmin):
        list_display = ('usuarios','salas',)