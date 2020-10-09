from django.shortcuts import render
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

# Create your views here.

def landingpage(request):
    questions = Question.objects.all()
    return render (request, "questionbox/landingpage.html", {"questions":questions})

# build views and login decorator when needed for question/answer list, create, search

def question_list(request):
    question=Question.objects.all()
    return render (request, 'question/question_list.html')

def question_create(request):
    question=Question.objects.all()
    return render (request, 'question/question_create.html')

def question_search(request):
    question=Question.objects.all()
    return render (request, 'question/question_search.html')

def answer_list(request):
    answer=Answer.objects.all()
    return render (request, 'answer/answer_list.html')

def answer_create(request):
    answer=Answer.objects.all()
    return render (request, 'answer/answer_create.html')

def answer_search(request):
    answer=Answer.objects.all()
    return render (request, 'answer/answer_search.html')

    # need to use variables for question and answer, decide where to use questionform/answerform