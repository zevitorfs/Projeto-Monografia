from pyexpat import model
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from . import models


class login(ListView):
    model = models.login
    template_name = 'login/conta.html'
