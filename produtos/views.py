from django.shortcuts import render  # Código original do Django
from django_filters.rest_framework import (
    DjangoFilterBackend,  # Aula 20: Importação do backend de filtros django-filter
)
from rest_framework import viewsets  # Importação padrão do DRF para ViewSets
from rest_framework.filters import (  # Aula 20: Importação dos filtros de busca e ordenação do DRF
    OrderingFilter,
    SearchFilter,
)

from .models import Produto  # Aula 19: Importação do modelo Produto
from .serializers import (
    ProdutoSerializer,  # Aula 19: Importação do ProdutoSerializer
)


# ---  AULA 19 E 20: IMPLEMENTAÇÃO DA VIEWSET DE PRODUTOS COM FILTROS ---
class ProdutoViewSet(viewsets.ModelViewSet):  # Aula 19: Criação da ViewSet com operações CRUD completas
    queryset = Produto.objects.all()  # Aula 19: Definição da busca de todos os produtos
    serializer_class = ProdutoSerializer  # Aula 19: Associação da ViewSet com o ProdutoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Aula 20: Habilita backends de filtro, busca e ordenação  # noqa: RUF012
    filterset_fields = ['estoque']  # Aula 20: Permite filtrar exatamente pelo valor do estoque  # noqa: RUF012
    search_fields = ['nome', 'descricao']  # Aula 20: Permite busca por texto no nome ou descrição  # noqa: RUF012
    ordering_fields = ['preco', 'criado_em']  # Aula 20: Permite ordenar listagens por preço ou data de criação  # noqa: RUF012
