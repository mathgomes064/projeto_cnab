from rest_framework import serializers
from .models import Transactions
import uuid


class TransactionsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    tipo = serializers.IntegerField()
    data = serializers.DateField()
    valor = serializers.IntegerField()
    cpf = serializers.CharField(max_length=11)
    cartao = serializers.CharField(max_length=20)
    hora = serializers.TimeField()
    donoDaLoja = serializers.CharField(max_length=30)
    nomeLoja = serializers.CharField(max_length=30)

    def create(self, validated_data: dict):
        return Transactions.objects.create(**validated_data)
