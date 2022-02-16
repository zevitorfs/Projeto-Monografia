from pyexpat import model
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models


class Perfil(ListView):
    model = models.perfil
    template_name = 'perfil/meuperfil.html'


class Criar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('CRIAR')


class Autalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Autalizar')


class Login(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Login')


class Logout(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Logout')
