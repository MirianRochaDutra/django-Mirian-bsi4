from django.contrib import admin

from .models import Produto  # Aula 18: Importação do modelo Produto


# --- AULA 18: REGISTRO DO MODELO NO ADMIN ---
@admin.register(Produto)  # Aula 18: Decorador para registrar Produto no painel admin
class ProdutoAdmin(
    admin.ModelAdmin
):  # Aula 18: Classe de personalização da interface admin
    list_display = (
        "id",
        "nome",
        "preco",
        "estoque",
        "criado_em",
    )  # Alteração: Colunas exibidas na listagem
    search_fields = ("nome",)  # Aula 18: Campo habilitado para busca
    list_filter = ("criado_em",)  # Aula 18: Filtro por data de criação
