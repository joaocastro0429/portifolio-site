from django.shortcuts import render
from django.http import HttpResponse






def home(request):
    projects = [
        {
            'title': 'Projeto 1',
            'description': 'Descrição do primeiro projeto.',
            'image': '/static/imagens/projeto1.jpg' 
        },
        {
            'title': 'Projeto 2',
            'description': 'Descrição do segundo projeto.',
            'image': '/static/imagens/projeto2.jpg'
        },
        {
            'title': 'Projeto 3',
            'description': 'Descrição do terceiro projeto.',
            'image': '/static/imagens/projeto3.jpg'
        },
    ]
    
    return render(request, 'portifolio.html', {'projects': projects})
