from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'posts/pages/home.html', context={
        'name': 'Willian Souza dos Santos',
        }) # passando o caminho e uma subpasta, criamos um namespace para não colidir com nomes iguais no projeto

