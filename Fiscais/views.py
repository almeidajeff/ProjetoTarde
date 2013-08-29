from models import *
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from forms import *

def lista(request):
    fiscais = Fiscal.objects.all()
    
    for f in fiscais:
        salas = f.salas
        
    
    template = get_template('lista.html')
    variables = Context({
                         'fiscais': fiscais,
                         })
    output = template.render(variables)
    
    return HttpResponse(output)

def add_fiscal(request):
    pass

