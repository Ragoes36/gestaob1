from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from polls.models import Choice, Question
from django.urls import reverse
from django.views import generic
from django.contrib import messages


@method_decorator(login_required(login_url='login'), name='dispatch')
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
    
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     try:
#         selected_choice = question.choice_set.get(pk = request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Exiba novamente o formulário de votação da pergunta.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': 'Você não selecionou uma opção.',
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args = (question.id,)))


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    # Verificar se a enquete já foi votada pelo usuário nesta sessão
    if 'voted_question_{}'.format(question_id) in request.session:
        # Adicionar mensagem de erro
        messages.error(request, 'Voto não autorizado.')
        return HttpResponseRedirect(reverse('polls:index'))  # Redirecionar para a página inicial
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Exiba novamente o formulário de votação da pergunta com uma mensagem de erro.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'Você não selecionou uma opção.',
        })
    else:
        if request.user.is_authenticated:
            # Processar o voto
            selected_choice.votes += 1
            selected_choice.save()
            
            # Registrar que o usuário já votou nesta enquete nesta sessão
            request.session['voted_question_{}'.format(question_id)] = True
            
            # Redirecionar para a página de resultados ou outra página de sua escolha
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        else:
            # Se o usuário não estiver autenticado, você pode lidar com isso de acordo com sua lógica de negócios.
            # Aqui estou apenas redirecionando para a página de login
            return HttpResponseRedirect(reverse('login'))
