from django.shortcuts import redirect, render
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def landingpage(request):
    questions = Question.objects.all()
    return render (request, "questionbox/landingpage.html", {"questions":questions})

# build views and login decorator when needed for question/answer list, create, search

def question_list(request):
    question=Question.objects.all()
    display = {'questions':question}
    return render (request, 'questionbox/question_list.html', display)

@login_required
def question_create(request):
    form = QuestionForm(data=request.POST)
    if form.is_valid():
        question = form.save
        question.user=request.user
        question.save()
        return redirect (to="question_list", pk=question.pk)
    form = QuestionForm()
    return render (request, 'questionbox/question_create.html', {'form': form})

@login_required
def question_search(request):
    question=Question.objects.all()
    return render (request, 'questionbox/question_search.html')
# need some help with this view

@login_required
def answer_list(request):
    answer=Answer.objects.all()
    display = {'answers':answer}
    return render (request, 'questionbox/answer_list.html', display)

@login_required
def answer_create(request):
    form = AnswerForm(data=request.POST)
    if form.is_valid():
        answer = form.save
        answer.user=request.user
        answer.save()
        return redirect (to="answer_list", pk=answer.pk)
    form = QuestionForm()
    return render (request, 'questionbox/answer_create.html', {'form':form})

@login_required
def answer_search(request):
    answer=Answer.objects.all()
    return render (request, 'questionbox/answer_search.html')
# will need to revise along with question search
