from django.urls import include, path
from .views import *


urlpatterns = [
path('index/', index, name='main-view'),
path('quiz/<int:id>/', quiz_attempt, name='quiz_attempt'),
#path('submit_quiz/', quiz_attempt, name='submit_quiz'),
]