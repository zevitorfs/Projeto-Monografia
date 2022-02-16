from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models


class ListaArquivo(ListView):
    model = models.anexar_arquivo
    template_name = 'anexar_arquivo/lista.html'


class DetalheArquivo(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')
