from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    quiz_list = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quiz_list': quiz_list})

def quiz_attempt(request, id):
    quiz = Question.objects.filter(quiz_id=id)
    return render(request, 'quiz.html', {'quiz': quiz})

# def submit_quiz(request):
#     return HttpResponse("submit")