from django.shortcuts import render, redirect
from django.conf import settings
from .models import Departamento
from django.utils.crypto import get_random_string
import random


def pruebas_models(request):
    for i in range(0,10):
        # genera descripcion y departamento de forma aleatoria
        descripcion=get_random_string(length=15)
        departamento=random.randint(100,999)
        
        # instanciamos departamento con los datos anteriores
        departamento1 = Departamento(nombre=departamento, 
					descripcion=descripcion, 
					)
        departamento1.save()
        
    departamento1 = Departamento.objects.values()
    context = {'departamento2': departamento1}
    return render(request, 'app/index.html', context)


# Create your views here.
