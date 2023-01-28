from django.db import models


class Transactions(models.Model):
    tipo = models.IntegerField()
    data = models.DateField()
    valor = models.IntegerField()
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=20)
    hora = models.TimeField()
    donoDaLoja = models.CharField(max_length=30)
    nomeLoja = models.CharField(max_length=30)
