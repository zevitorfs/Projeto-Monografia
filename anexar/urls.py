from django.urls import path
from . import views  # importante

app_nome = 'anexar'
urlpatterns = [
    path('Anexar', views.CampoCreate.as_view(), name="Anexar"),

]
