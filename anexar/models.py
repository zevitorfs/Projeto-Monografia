from django.db import models
from django.utils.text import slugify
import os


class anexar(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Tema da monografia')
    descricao = models.TextField(verbose_name='Resumo')
    arquivo_pdf = models.FileField(upload_to='uploads/', default='')
    publicacao = models.DateField(
        verbose_name='Data de Publicação', default='')
    slug = models.SlugField(unique=True, blank=True, null=True)

    # @staticmethod
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)
