from django.http import HttpResponse
from django.shortcuts import render

# Quando digita a url do site, o usuário faz um REQUEST
# Logo, o servidor deve retornar uma RESPONSE
# O comando path retorna essa requisição e devemo tratá-la
# na nossa função my_view() Vamos importar a HttpRespons


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Samuel Ágap',
    })
    # O Django já sabe que vai buscar esse .html na pasta "templates" do app


def sobre(request):
    return HttpResponse("Sobre")


def contato(request):
    return render(request, 'recipes/contato.html', context={
        'name': 'Virgínia Silva',
    })
