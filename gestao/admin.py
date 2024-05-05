from django.contrib import admin
from gestao.models import Segmento, Empresas, Sugestoes, Reclamacoes, AvaliacaoPrestadorServico



class SegmentoAdmin(admin.ModelAdmin):
    list_display = ('opcoes',)
    search_fields = ('opcoes',)


class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'segmento', 'contatos', 'site', 'descrição',)
    search_fields = ('nome', 'segmento', 'contatos', 'site', 'descrição',)


class SugestoesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'condominio', 'contato', 'unidade', 'incoveniente', 'sugestao_de_melhoria',)
    search_fields = ('nome', 'condominio', 'contato', 'unidade', 'incoveniente', 'sugestao_de_melhoria',)


class ReclamacoesAdmin(admin.ModelAdmin):
    list_display = ('reclamante', 'condominio', 'contato', 'unidade', 'reclamado', 'ocorrencia',)
    search_fields = ('reclamante', 'condominio', 'contato', 'unidade', 'reclamado', 'ocorrencia',)


class AvalicaoPrestadorServicoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'classificacao', 'comentario',)
    search_fields = ('empresa', 'classificacao', 'comentario',)


admin.site.register(Segmento, SegmentoAdmin)
admin.site.register(Empresas, EmpresasAdmin)
admin.site.register(Sugestoes, SugestoesAdmin)
admin.site.register(Reclamacoes, ReclamacoesAdmin)
admin.site.register(AvaliacaoPrestadorServico, AvalicaoPrestadorServicoAdmin)
