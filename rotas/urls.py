from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'rotas.views.index'),
    #rota de url pelo id de cada rota de trem
    url(r'^rotas/(?P<rota_id>\d+)$', 'rotas.views.exibir')
)
