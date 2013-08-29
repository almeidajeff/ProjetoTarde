from django import forms
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect


class add_Fiscal(forms.Form):
    fiscal_id = forms.IntegerField()
    sala_id = forms.IntegerField()
        
        
def fiscal(request):
    if request.method == 'POST':
        form = add_Fiscal(request.POST)
        
        if form.is_valid():
            import pdb;pdb.set_trace();
            
            return HttpResponseRedirect('/obrigado')
    else:
        form = add_Fiscal()
            
    return render_to_response(
                              'fiscal.html',
                              locals(),
                              context_instance=RequestContext(request),
                              )       
def obrigado(request):
    return render_to_response(
                              'obrigado.html',
                              locals(),
                              context_instance=RequestContext(request),
                              )       
    