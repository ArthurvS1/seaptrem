from django.shortcuts import render
from rotas.models import Rota
def index(request):
    return render(request, 'index.html')

def exibir(request, rota_id):
    rota = Rota()

    if rota_id == '1':
        rota = Rota('Mossoro', '0', '0,50')
    if rota_id == '2':
        rota = Rota('Tibau', '40', '50,00')

    return render(request, 'rota.html', { "rota": rota })
