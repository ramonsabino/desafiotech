import random
from django.shortcuts import render
from .models import Usuario
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

# import random
# import json
# Create your views here.

def index(request):
  if request.method == 'POST':

    # charlist = list('abcdefghijklmnopqrstuvwxyz1234567890')
    # length = 10

    # gensenha = ''
    # for x in range(length):
    #   senha += random.choice(charlist)

    nome = request.POST['nome']
    email = request.POST['email']
    data_nascimento = request.POST['data_nascimento']
    senha = request.POST['senha']

    obj = Usuario()
    obj.nome = nome
    obj.email = email
    obj.data_nascimento = data_nascimento
    obj.senha = make_password(senha)
    obj.save()
  return render(request,'index.html')


def usuarios(request):
  data = serializers.serialize("python", Usuario.objects.all())
  
  context = {
    'data':data,
  }
  return render(request, 'usuarios.html', context)

def json(request):
  data = list(Usuario.objects.values())
  return JsonResponse(data, safe=False)

