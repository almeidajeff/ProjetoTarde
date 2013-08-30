from django import forms
from .models import Funcionario

class FuncionarioForm(form.ModelForm):
    class Meta:
        model = Funcionario