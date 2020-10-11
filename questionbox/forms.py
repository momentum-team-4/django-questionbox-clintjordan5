from django import forms
# from django.forms import ModelForm
from .models import Question
from .models import Answer

# build question and answer model

class QuestionForm (forms.ModelForm):
    class Meta:
        model = Question
        fields = [
                'title',
                'body',
            ]

class AnswerForm (forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
                'title',
                'body',
            ]