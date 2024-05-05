from django.contrib import admin
from django.urls import path, include
from gestao.views import PaginaInicialView, Empresas, CadastrarEmpresas, Sugestoes, Reclamacoes, Avaliacao, visualizacao
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Formulários
    path('registro/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # gestao
    path('', PaginaInicialView.as_view(), name='pagina_inicial'),
    path('sugestoes/', Sugestoes.as_view(), name='sugestoes'),
    path('reclamacoes/', Reclamacoes.as_view(), name='reclamacoes'),
    path('nova_empresa/', CadastrarEmpresas.as_view(), name='nova_empresa'),
    path('empresas/', Empresas.as_view(), name='empresas_list'),
    path('avaliacoes/', Avaliacao.as_view(), name='avaliacoes'),
    path('visu/', visualizacao.as_view(), name='visu'),
    # polls
    path("polls/", include("polls.urls")),
    
]
