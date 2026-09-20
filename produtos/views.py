from django.shortcuts import render  # Código original do Django
from django_filters.rest_framework import (
    DjangoFilterBackend,  # Importação do backend de filtros django-filter
)
from rest_framework import viewsets  # Importação padrão do DRF para ViewSets
from rest_framework.filters import (  # Importação dos filtros de busca e ordenação do DRF
    OrderingFilter,
    SearchFilter,
)
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,  # Aula 25: Permissão de leitura pública e escrita apenas autenticada
)

from .models import Produto  # Importação do modelo Produto
from .serializers import (
    ProdutoSerializer,  # Importação do ProdutoSerializer
)


# --- AULA 19, 20, 23 & 25: IMPLEMENTAÇÃO DA VIEWSET DE PRODUTOS ---
class ProdutoViewSet(viewsets.ModelViewSet):  # Aula 19: Criação da ViewSet com operações CRUD completas
    queryset = Produto.objects.all()  # Aula 19: Definição da busca de todos os produtos
    serializer_class = ProdutoSerializer  # Aula 19: Associação da ViewSet com o ProdutoSerializer

    # --- AULA 25: CONFIGURAÇÃO DE PERMISSÕES ---
    permission_classes = [IsAuthenticatedOrReadOnly]  # Aula 25: Permite leitura para todos e escrita para autenticados

    # --- AULA 23: CONFIGURAÇÃO DE FILTROS, BUSCA E ORDENAÇÃO ---
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Aula 23: Backends de filtro
    filterset_fields = ['categoria', 'estoque']  # Aula 23: Filtro exato por categoria e estoque
    search_fields = ['nome', 'descricao']  # Aula 23: Busca parcial por nome e descrição
    ordering_fields = ['preco', 'nome', 'criado_em']  # Aula 23: Ordenação por preço, nome ou data
    ordering = ['-criado_em']  # Aula 23: Ordenação padrão (mais recentes primeiro)