from rest_framework import serializers  # Importação padrão do DRF

from .models import Produto  # Alteração: Importação do modelo Produto conforme Aula 19


# --- AULA 19 & 22: DEFINIÇÃO E VALIDAÇÕES DO SERIALIZER DO PRODUTO ---
class ProdutoSerializer(serializers.ModelSerializer):  # Aula 19: Classe serializadora do Produto
    class Meta:  # Aula 19: Classe interna de metadados do serializer
        model = Produto  # Aula 19: Associação direta com o model Produto
        fields = "__all__"  # Aula 19: Inclusão de todos os campos do modelo no JSON

    # --- AULA 22: VALIDAÇÕES PERSONALIZADAS POR CAMPO ---
    def validate_preco(self, value):  # Aula 22: Método de validação específico para o campo 'preco'
        """Valida se o preço é estritamente maior que zero."""
        if value <= 0:  # Aula 22: Checa se o preço fornecido é menor ou igual a zero
            raise serializers.ValidationError(  # Aula 22: Dispara erro de validação do DRF
                "O preço do produto deve ser maior que zero."
            )
        return value  # Aula 22: Retorna o valor validado se passar na regra

    def validate_nome(self, value):  # Aula 22: Método de validação específico para o campo 'nome'
        """Valida se o nome possui pelo menos 2 caracteres."""
        if len(value.strip()) < 2:  # Aula 22: Remove espaços e checa o tamanho mínimo do nome
            raise serializers.ValidationError(  # Aula 22: Dispara erro de validação do DRF
                "O nome do produto deve ter pelo menos 2 caracteres."
            )
        return value  # Aula 22: Retorna o valor validado se passar na regra