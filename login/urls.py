from django.urls import path
from . import views

app_nome = 'pessoa'
urlpatterns = [
    path('Login', views.login.as_view(), name="login"),
]
