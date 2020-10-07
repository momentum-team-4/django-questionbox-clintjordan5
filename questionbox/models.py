from django.db import models
from users.models import User


# Create your models here.

class Question (models.Model):
    title = models.CharField (max_length=255)
    body = models.TextField (blank=False)
    author = models.ForeignKey(to=user)

class Answer (models.Model):
    title = models.CharField (max_length=255)
    body = models.TextField (blank=False)
    author = models.ForeignKey(to=user)
    # question=models.ForeignKey(to=question, on-delete=models.CASCADE. related_name="answers")






"""
list of model ideas for project

users 
- create user 
- login
starred_questions=models.manytomanyfield
to=question, related_name="starred_by"

question 
- body
- title
- asked at
- author - which user asked question

answer
- body
- title
- answered at
- author - which user answered question
- constraint - is answer correct? true/false
"""