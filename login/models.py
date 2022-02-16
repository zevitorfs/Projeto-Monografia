from django.db import models


class login(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome de usuario')
    senha = models.CharField(max_length=255, verbose_name='Senha')
