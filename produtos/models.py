from django.db import models


# ---  AULA 18: DEFINIÇÃO DO MODELO PRODUTO ---
class Produto(models.Model):  # Aula 18: Criação da entidade Produto 
    nome = models.CharField(max_length=100)  # Aula 18: Campo de texto para o nome do produto 
    descricao = models.TextField(blank=True, null=True)  # Aula 18: Campo de texto longo para descrição opcional 
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Aula 18: Campo decimal para o preço do produto 
    estoque = models.IntegerField(default=0)  # Aula 18: Campo inteiro para quantidade em estoque 
    criado_em = models.DateTimeField(auto_now_add=True)  # Aula 18: Data/hora de criação automática 
    atualizado_em = models.DateTimeField(auto_now=True)  # Aula 18: Data/hora de atualização automática 

    def __str__(self):  # Aula 18: Método para exibição amigável do objeto 
        return self.nome  # Aula 18: Retorna o nome do produto 