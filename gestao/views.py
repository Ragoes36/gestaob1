from gestao.models import Empresas, Sugestoes, Reclamacoes, AvaliacaoPrestadorServico
from gestao.forms import EmpresasModelForm, SugestoesModelForm, ReclamaçoesModelForm, AvaliacoesModelForm
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PaginaInicialView(TemplateView):
    template_name = 'pagina_inicial.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class Empresas(ListView):
    model = Empresas
    template_name = 'empresas.html'
    context_object_name = 'empresas'

    def get_queryset(self):
        empresas = super().get_queryset().order_by('nome')
        search = self.request.GET.get('search')
        if search:
            empresas = Empresas.objects.filter(model__incontains=(search))
        return empresas


@method_decorator(login_required(login_url='login'), name='dispatch')
class CadastrarEmpresas(CreateView):
    model = Empresas
    form_class = EmpresasModelForm
    template_name = 'cadastrar_empresas.html'
    success_url = '/nova_empresa/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class Sugestoes(CreateView):
    model = Sugestoes
    form_class = SugestoesModelForm
    template_name = 'sugestoes.html'
    success_url = '/sugestoes/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class Reclamacoes(CreateView):    
    model = Reclamacoes
    form_class = ReclamaçoesModelForm
    template_name = 'reclamacoes.html'
    success_url = '/reclamacoes/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class Avaliacao(CreateView):
    model = AvaliacaoPrestadorServico
    form_class = AvaliacoesModelForm
    template_name = 'avaliacoes.html'
    success_url = '/avaliacoes/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class visualizacao(ListView):
    model = AvaliacaoPrestadorServico
    template_name = 'visu.html'
    context_object_name = 'empresas'


