from django.shortcuts import render  # Código original do Django
from rest_framework import viewsets  # Importação padrão do DRF para ViewSets

from .models import Produto  # Aula 19: Importação do modelo Produto
from .serializers import (
    ProdutoSerializer,  # Aula 19: Importação do ProdutoSerializer
)


# ---  AULA 19: IMPLEMENTAÇÃO DA VIEWSET DE PRODUTOS ---
class ProdutoViewSet(viewsets.ModelViewSet):  # Aula 19: Criação da ViewSet com operações CRUD completas
    queryset = Produto.objects.all()  # Aula 19: Definição da busca de todos os produtos
    serializer_class = ProdutoSerializer  # Aula 19: Associação da ViewSet com o ProdutoSerializer
    
