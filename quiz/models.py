from django.db import models



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
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return  self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE )
    correct_ans = models.CharField(max_length=255)
    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        
    def __str__(self):
        return  self.correct_ans

