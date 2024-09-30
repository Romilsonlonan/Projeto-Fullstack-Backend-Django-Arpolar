import random
import re
from django.db import models

from authentication.validators import validar_cpf 

# Modelo Colaborador
class Colaborador(models.Model):
    """
    Modelo que representa um colaborador na empresa.
    """
    imagem = models.ImageField(upload_to="icones", null=True, blank=True)  # Foto é opcional
    nome = models.CharField(max_length=30)
    cpf = models.CharField(
        max_length=14,  # Tamanho 14 para suportar o formato xxx.xxx.xxx-xx
        unique=True,  # CPF deve ser único
        validators=[validar_cpf],  # Adiciona o validador de CPF
        help_text="Digite o CPF no formato xxx.xxx.xxx-xx"
    )
    data_nasc = models.DateField()  # Campo para a data de nascimento
    telefone_contato = models.CharField(max_length=15, blank=True, null=True)  # Telefone de contato
    email = models.EmailField(max_length=254, blank=True, null=True)  # E-mail
    funcao = models.CharField(max_length=50, blank=True, null=True)  # Função (profissão)
    data_inicio = models.DateField()  # Data de início da matrícula
    data_fim = models.DateField(null=True, blank=True)  # Data de término
    historico_funcoes = models.TextField(null=True, blank=True)  # Histórico de funções
    observacoes = models.TextField(max_length=2000, blank=True, null=True)  # Campo para observações
    add_matricula = models.CharField(max_length=5, unique=True, blank=True, null=True)  # Matrícula
    senha = models.CharField(max_length=6, unique=True, blank=True, null=True, editable=False)  # Senha de 6 dígitos


    def __str__(self):
        return self.nome  # Exibe o nome do colaborador

    def save(self, *args, **kwargs):
        """Gera a senha automaticamente se não estiver definida."""
        if not self.senha:
            self.senha = self.gerar_senha()
        super().save(*args, **kwargs)

    def gerar_senha(self):
        """Gera uma senha de 6 números únicos"""
        while True:
            senha = ''.join(random.sample('0123456789', 6))
            if not Colaborador.objects.filter(senha=senha).exists():
                return senha
