from rest_framework import serializers
from questionbox.models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
        'title', 
        'body',
        'author',
        'date',
        ]

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.author = validated_data.get('author', instance.author)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
        'title', 
        'body',
        'author',
        'question',
        'date',
        ]

    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.author = validated_data.get('author', instance.author)
        instance.question = validated_data.get('question', instance.question)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

# class Answer (models.Model):
#     title = models.CharField (max_length=255)
#     body = models.TextField (blank=False)
#     author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="answers", null=True)
#     question = models.ForeignKey(to=Question, on_delete=models.CASCADE, related_name="answers", null=True)
#     # have answer reference the original question and show author of both with related name
#     date = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         return f'{self.title}'
#         # is this correct? should it be self.body?
