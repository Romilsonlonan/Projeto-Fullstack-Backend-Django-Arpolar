from django.contrib import admin
from .models import Colaborador

class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nasc', 'cpf', 'telefone_contato', 'email', 'funcao', 'data_inicio', 'data_fim', 'add_matricula', 'senha')
    search_fields = ('nome', 'cpf', 'email', 'funcao')
    list_filter = ('data_nasc', 'funcao')
    readonly_fields = ('senha',)  # Torna 'senha' somente leitura para segurança
    fieldsets = (
        (None, {
            'fields': (
                'imagem', 'nome', 'cpf', 'data_nasc', 'telefone_contato', 
                'email', 'funcao', 'data_inicio', 'data_fim', 
                'historico_funcoes', 'observacoes', 'add_matricula', 'senha'
            )
        }),
    )

admin.site.register(Colaborador, ColaboradorAdmin)

