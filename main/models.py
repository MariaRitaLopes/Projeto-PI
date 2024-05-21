from django.db import models

class Animais(models.Model):
    nome = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    sexo = models.CharField(max_length=255)
    idade = models.CharField(max_length=255)
    cor = models.CharField(max_length=255)
    castrado = models.CharField(max_length=255)
    