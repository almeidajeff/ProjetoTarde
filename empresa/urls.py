# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^criar/$', views.FuncionarioCreateView.as_view(), name='criar'),
                       url(r'^atualizar/(?P<pk>\d+)\$', views.FuncionarioUpdateView.as_view(), name='atualizar'),
                       )