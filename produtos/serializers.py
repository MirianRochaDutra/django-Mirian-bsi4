from rest_framework import serializers  # Importação padrão do DRF

from .models import Produto  # Alteração: Importação do modelo Produto conforme Aula 19


# --- AULA 19: DEFINIÇÃO DO SERIALIZER DO PRODUTO ---
class ProdutoSerializer(serializers.ModelSerializer):  # Aula 19: Classe serializadora do Produto
    class Meta:  # Aula 19: Classe interna de metadados do serializer
        model = Produto  # Aula 19: Associação direta com o model Produto
        fields = "__all__"  # Aula 19: Inclusão de todos os campos do modelo no JSON
