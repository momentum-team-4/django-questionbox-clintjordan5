from django.db import models
# from users.models import User


# Create your models here.

class Question (models.Model):
    title = models.CharField (max_length=255)
    body = models.TextField (blank=False)
    # author = models.ForeignKey(to=user)

class Answer (models.Model):
    title = models.CharField (max_length=255)
    body = models.TextField (blank=False)
    # author = models.ForeignKey(to=user)
    # question=models.ForeignKey(to=question, on-delete=models.CASCADE. related_name="answers")