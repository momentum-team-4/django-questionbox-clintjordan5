from django.shortcuts import redirect, render, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# landing page
# question list, create, search, delete, detail
# answer list, create, search, delete, detail

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
    if request.method == "GET":
        form = QuestionForm()
    else:
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect(to='question_list')
    return render (request, 'questionbox/question_create.html', {'form': form})

@login_required
def question_search(request):
    question=Question.objects.all()
    return render (request, 'questionbox/question_search.html')
# need some help with this view

@login_required
def question_delete(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    if request.method == "POST":
        question.delete()
        return redirect("questions_list")
    return render(request, "questionbox/question_delete.html", {'questions': question} )

def question_detail(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    answers = question.answers.all()
    form = AnswerForm()
    if request.method == "POST":
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect(to="question_detail", pk=question_pk)
    return render(request, "questionbox/question_detail.html", {
        'question': question,
        'answers': answers,
        'question_pk': question_pk,
    })

@login_required
def answer_list(request):
    answer=Answer.objects.all()
    display = {'answers':answer}
    return render (request, 'questionbox/answer_list.html', display)


@login_required
def answer_create(request, question_pk):
    if request.method == 'GET':
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        question = get_object_or_404(Question, pk=question_pk)
        if form.is_valid():
            print(form)
            answer = form.save(commit=False)
            answer.author = request.user
            answer.answered_for = question
            answer.save()
            return redirect(to='question_detail', question_pk=question_pk)
    return render(request, 'questionbox/answer_create.html',
    {'form':form, 'question_pk': question_pk})

@login_required
def answer_search(request):
    answer=Answer.objects.all()
    return render (request, 'questionbox/answer_search.html')
# will need to revise along with question search


@login_required
def answer_delete(request, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    if request.method == "POST":
        question = answer.answered_for.get()
        question_pk = question.pk
        answer.delete()
        return redirect('question_detail', question_pk=question_pk)
    return render(request, "questionbox/answer_delete.html", {'answer':answer})

def answer_detail(request, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    return render(request, 'questions/answer_detail.html', {'answer':answer})