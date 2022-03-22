import random

from django.db import models

# Create your models here.

class Usuario(models.Model):
  nome = models.CharField(max_length=50)
  email = models.CharField(max_length=30)
  data_nascimento = models.DateField()
  senha = models.CharField(max_length=50)

