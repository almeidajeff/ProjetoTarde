from django.conf.urls import patterns, include, url
from views import lista

urlpatterns = patterns('',
    (r'^lista/$', lista),
)