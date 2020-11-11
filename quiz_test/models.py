from django.db import models
from django.contrib.auth.models import User
import jsonfield


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=30)

    class Meta:
        pass

CORRECT_CHOICES =(
    ("1", "Option1"),
    ("2", "Option2"),
    ("3", "Option3"),
    ("4", "Option4")
)

class Question(models.Model):
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=30)
    option2 = models.CharField(max_length=30)
    option3 = models.CharField(max_length=30)
    option4 = models.CharField(max_length=30)
    correct = models.CharField(max_length=1, choices=CORRECT_CHOICES)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    quiz_result = jsonfield.JSONField()
