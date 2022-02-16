from dataclasses import field, fields
from pyexpat import model
from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
# class anexar(ListView):


class CampoCreate(CreateView):
    model = models.anexar
    fields = ['nome', 'descricao', 'arquivo_pdf', 'publicacao']
    template_name = 'anexar/arquivo.html'
    success_url = reverse_lazy('lista')
