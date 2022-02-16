# Generated by Django 4.0.2 on 2022-02-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anexar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Tema da monografia')),
                ('descricao', models.TextField(max_length=255, verbose_name='Resumo')),
                ('arquivo_pdf', models.FileField(default='', upload_to='uploads/')),
                ('publicacao', models.DateField(default='', verbose_name='Data de Publicação')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
    ]
