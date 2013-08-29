from models import *
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from forms import *

def lista(request):
    obj_fiscais = Fiscal.objects.all()
    fiscais = []
    for f in obj_fiscais:
        s = []
        #import pdb;pdb.set_trace()
        salas = f.salas.values()
        for sl in salas:
            s.append(sl)
        fiscais.append({'fiscal':f.usuario.username,'salas':s})
    
    template = get_template('lista.html')
    variables = Context({
                         'fiscais': fiscais,
                         })
    output = template.render(variables)
    
    return HttpResponse(output)

def add_fiscal(request):
    pass

