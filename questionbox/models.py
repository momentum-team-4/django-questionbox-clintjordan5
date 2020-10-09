from django.db import models
from users.models import User


# Create your models here.

class Question (models.Model):
    title = models.CharField (max_length=255)
    body = models.TextField (blank=False)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="questions", null=True)

    def __str__(self):
        return f'{self.title}'

class Answer (models.Model):
    title = models.CharField (max_length=255)
    body = models.TextField (blank=False)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="answers", null=True)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name="answers", null=True)

    def __str__(self):
        return f'{self.title}'
        # is this correct? should it be self.body?
