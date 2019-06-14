from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question
from .forms import ChoiceForm
from django.utils import timezone



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def myquestion(request):
    return render(request, 'polls/myquestion.html')


def detail(request, question_id):
    if request.method == 'GET':
        question = get_object_or_404(Question, pk=question_id)
        form = ChoiceForm()
        d = {'question': question,
             'form': form
             }
        return render(request, 'polls/detail.html', d)

    elif request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        form = ChoiceForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.save()
            return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "必ず1つは選択してください",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def insert(request):
    q = Question(question_title=request.POST['text_title'], question_text=request.POST['text_name'],
                 pub_date=timezone.now())
    q.save()

    return HttpResponseRedirect(reverse('polls:index'))






