from rest_framework import serializers  # Importação padrão do DRF

from .models import Produto  # Importação do modelo Produto


# --- AULA 19, 22 & 26: DEFINIÇÃO E VALIDAÇÕES DO SERIALIZER DO PRODUTO ---
class ProdutoSerializer(serializers.ModelSerializer):  # Aula 19: Classe serializadora do Produto
    # Aula 26: Campos declarados explicitamente como obrigatórios
    marca = serializers.CharField(required=True, max_length=50)
    estoque = serializers.IntegerField(required=True)  # Aula 26: Estoque inteiro e obrigatório

    class Meta:  # Aula 19: Classe interna de metadados do serializer
        model = Produto  # Aula 19: Associação direta com o model Produto
        fields = "__all__"  # Aula 19 & 26: Inclusão de todos os campos do modelo no JSON

    # --- AULA 26: VALIDAÇÕES PERSONALIZADAS (MARCA E ESTOQUE) ---
    def validate_marca(self, value):  # Aula 26: Método de validação do campo marca
        marca_limpa = value.strip()
        if len(marca_limpa) < 2:
            raise serializers.ValidationError(
                "A marca deve possuir entre 2 e 50 caracteres."
            )
        return marca_limpa

    def validate_estoque(self, value):  # Aula 26: Validação de estoque não negativo
        if value < 0:
            raise serializers.ValidationError("O estoque não pode ser negativo.")
        return value

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