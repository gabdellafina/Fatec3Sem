from django.urls import path
from . import views

urlpatterns = [
    path('', views.appHome, name='appHome'),
    path('cadastro/', views.cadastrar_user, name='cadastrar_user'),
    path('usuarios/', views.exibir_user, name='exibir_user'),
    path('cadastroProd/', views.cadastrar_prod, name='cadastrar_prod'),
]