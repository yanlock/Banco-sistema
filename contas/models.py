from django.db import models


class Pessoa(models.Model):
  nome = models.CharField(max_length=255)
  cpf = models.CharField(max_length=14)
 
