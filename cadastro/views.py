from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models


class Cadastrar(ListView):
    model = models.perfil
    template_name = 'cadastro/cadastrar.html'
