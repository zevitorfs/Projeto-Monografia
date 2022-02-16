from django.db import models
from django.contrib.auth.models import User


class perfil(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    email = models.EmailField(verbose_name='Email')
    descricao = models.TextField(verbose_name='Descrição sobre autor(a)')


def __str__(self):
    return f'{self.usuario}'
