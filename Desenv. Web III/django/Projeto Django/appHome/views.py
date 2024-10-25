from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from appHome.form_cadastro_user import FormCadastroUser
from django.contrib import messages
from appHome.models import Usuario
from appHome.form_cadastro_prod import FormCadastroProd

# Create your views here.

def appHome(request):
    return render(request, 'home.html')

def cadastrar_user(request):
    novo_user = FormCadastroUser(request.POST or None)
    if novo_user.is_valid():
        novo_user.save()
        messages.success(request, 'Cadastrado com sucesso!')
        return redirect('appHome')
    context = {
        "form": novo_user
    }
    return render(request, 'cadastro.html', context)

def exibir_user(request):
    usuarios = Usuario.objects.all().values()

    context = {
        'dados' : usuarios
    }

    return render(request, 'usuarios.html', context)

def cadastrar_prod(request):
    novo_prod = FormCadastroProd(request.POST or None)
    if novo_prod.is_valid():
        novo_prod.save()
        messages.success(request, 'Cadastrado com sucesso!')
        return redirect('appHome')
    context = {
        "form": novo_prod
    }
    return render(request, 'cadastroProd.html', context)