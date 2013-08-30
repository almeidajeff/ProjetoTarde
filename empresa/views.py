# -*- coding: utf-8 -*-

from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import CreateView, UpdateView
from models import Funcionario
from forms import FuncionarioForm
from reportlab.pdfgen import canvas

class FuncionarioCreateView(CreateView):
    model = Funcionario
    sucesso_url = 'ok.html'
    form_class = FuncionarioForm
    
class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    sucesso_url = 'update.html'
    form_class = FuncionarioForm
    
def hello_pdf(request):
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
    p = canvas.Canvas(response)
    p.drawString(100,100,'Olá palavra!!')
    p.showPage()
    p.save()
    return response
    
    
