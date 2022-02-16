from email.policy import default
from django.db import models
from django.utils.text import slugify
import os


"""
    Produto:
            Produto:
                nome - Char
                descricao_curta - Text
                descricao_longa - Text
                imagem - Image
                slug - Slug
                preco_marketing - Float
                preco_marketing_promocional - Float
                tipo - Choices
                    ('V', 'Variável'),
                    ('S', 'Simples'),
                    descricao = models.TextField(verbose_name='Resumo')
    arquivo_pdf = models.FileField(upload_to='uploads/')
    publicacao = models.DateField(verbose_name='Data de Publicação')
    slug = models.SlugField(unique=True, blank=True, null=True)

    # @staticmethod
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)
"""


class anexar_arquivo(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Tema da monografia')
    descricao = models.TextField(verbose_name='Resumo')
    arquivo_pdf = models.FileField(upload_to='uploads/')
    publicacao = models.DateField(
        verbose_name='Data de Publicação')
    slug = models.SlugField(unique=True, blank=True, null=True)

    # @staticmethod
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)
