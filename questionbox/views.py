from django.shortcuts import render
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

# Create your views here.

def landingpage(request):
    questions = Question.objects.all()
    return render (request, "questionbox/landingpage.html", {"questions":questions})

# build views and login decorator when needed for question/answer list, create, search