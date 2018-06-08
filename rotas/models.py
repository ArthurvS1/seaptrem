from django.db import models

class Rota(object):

    def __init__(self, cidade='', distancia='', preco=''):
        self.cidade = cidade
        self.distancia = distancia
        self.preco = preco
