from django.shortcuts import render
from .models import Usuarios

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    # Salvar os dados da tela para um banco de dados
    novo_usuario = Usuarios()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')  
    novo_usuario.save()
    # Exibir todos os usuarios já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuarios.objects.all()
    }

    # Retornar os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)