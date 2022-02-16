from django.urls import path
from . import views

app_name = 'perfil'
urlpatterns = [

    path('Perfil/', views.Perfil.as_view(), name="Perfil"),
    path('Criar/', views.Criar.as_view(), name="Criar"),
    path('autalizar/', views.Autalizar.as_view(), name="Criar"),
    path('Login/', views.Login.as_view(), name="Criar"),
    path('Logout/', views.Logout.as_view(), name="Criar"),

]
