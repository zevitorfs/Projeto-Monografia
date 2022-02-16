from django.urls import path
from . import views
app_name = 'cadastro'
urlpatterns = [
    path('Cadastro', views.Cadastrar.as_view()),
]
