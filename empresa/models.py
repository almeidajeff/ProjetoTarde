from django.db import models
from django.db.models import fields
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.contrib.admin.options import ModelAdmin
from django import forms

class Departamento(models.Model):
    nome = fields.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nome
    
class Funcionario(User):
    departamento = ForeignKey(Departamento)
    chefe = ForeignKey('self', null=True, blank=True)
    
    def __unicode__(self):
        return self.first_name
        
    class Meta:
        verbose_name = 'Funcionario'

