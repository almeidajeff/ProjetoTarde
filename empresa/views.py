from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import CreateView, UpdateView
from models import Funcionario
from forms import FuncionarioForm


class FuncionarioCreateView(CreateView):
    model = Funcionario
    sucesso_url = 'ok.html'
    form_class = FuncionarioForm
    
class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    sucesso_url = 'update.html'
    form_class = FuncionarioForm
    
    
