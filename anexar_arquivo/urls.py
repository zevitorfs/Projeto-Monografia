from django.urls import path
from . import views

app_nome = 'arquivo'
urlpatterns = [
    path('', views.ListaArquivo.as_view(), name="lista"),
    path('<slug>', views.DetalheArquivo.as_view(), name="detalhe"),
]
