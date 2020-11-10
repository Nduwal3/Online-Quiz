from django.db import models
from django.contrib.auth.models import User



class Quiz(models.Model):
    """Model definition for Quiz."""
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizs'

    def __str__(self):
        return self.title 


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE )
    title = models.CharField(max_length=1000)
    correct_ans = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255, blank=True)
    option2 = models.CharField(max_length=255, blank=True)
    option3 = models.CharField(max_length=255, blank=True)
    option4 = models.CharField(max_length=255, blank=True)
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return  self.title

class QuizParticipant(models.Model):
    user = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    class Meta:
        verbose_name = 'QuizParticipant'
        verbose_name_plural = 'QuizParticipants'

    def __str__(self):
        return  self.user

