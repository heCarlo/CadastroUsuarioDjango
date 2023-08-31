from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    #Salvar os dados da tela para o banco de dados
    novoUsuario = Usuario()
    novoUsuario.nome = request.POST.get('nome') 
    novoUsuario.idade = request.POST.get('idade')    
    novoUsuario.save()

    #Exibir todos os usuários já cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #Retornar os dados para a página de listagem de usuários
    return render(request,'usuarios/usuarios.html',usuarios)