from django.contrib import admin
from models import *
from django.contrib.admin.options import ModelAdmin
from django import forms

class FuncionarioForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(FuncionarioForm, self).__init__(*args, **kwargs)
        self.fields['chefe'].queryset = \
        Funcionario.objects.filter(departamento=self.instance.departamento)
        
class FuncionarioAdmin(ModelAdmin):
    form = FuncionarioForm


admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Departamento)