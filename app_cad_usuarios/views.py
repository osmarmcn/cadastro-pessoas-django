from django.shortcuts import render
from .models import Usuario


def home(request):
    return render(request, 'usuarios/home.html')
# Create your views here.


def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #exibir todos os usuarios ja cdastrados em uma nov pagina

    usuarios = {
        'usuarios':Usuario.objects.all()
    }

    #retornar os dados para pagina de listagem
    return render(request,'usuarios/usuarios.html', usuarios)

 
    
