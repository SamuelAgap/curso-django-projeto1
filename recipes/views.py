from django.http import HttpResponse

# from django.shortcuts import render

# Quando digita a url do site, o usuário faz um REQUEST
# Logo, o servidor deve retornar uma RESPONSE
# O comando path retorna essa requisição e devemo tratá-la
# na nossa função my_view() Vamos importar a HttpRespons


def home(request):
    return HttpResponse("Home")


def sobre(request):
    return HttpResponse("Sobre")


def contato(request):
    return HttpResponse("Contato")
