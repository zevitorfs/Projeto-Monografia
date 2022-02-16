from django.db import models


class perfil(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    email = models.EmailField()
