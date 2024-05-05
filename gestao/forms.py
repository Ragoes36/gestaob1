from django import forms
from gestao.models import Empresas, Sugestoes, Reclamacoes, AvaliacaoPrestadorServico


class EmpresasModelForm(forms.ModelForm):
    class Meta:
        model = Empresas
        fields = '__all__'


class SugestoesModelForm(forms.ModelForm):
    class Meta:
        model = Sugestoes
        fields = ('nome', 'condominio', 'contato', 'unidade', 'incoveniente', 'sugestao_de_melhoria',)


class ReclamaçoesModelForm(forms.ModelForm):
    class Meta:
        model = Reclamacoes
        fields = ('reclamante', 'condominio', 'contato', 'unidade', 'reclamado', 'ocorrencia')


class AvaliacoesModelForm(forms.ModelForm):
    class Meta:
        model = AvaliacaoPrestadorServico
        fields = '__all__'
