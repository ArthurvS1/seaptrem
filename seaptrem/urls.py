from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #redirecionando para o arquivo perfis/urls.py
    url(r'^', include('perfis.urls'))
)
