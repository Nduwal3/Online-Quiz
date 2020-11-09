from django.shortcuts import render, get_object_or_404

from .models import Quiz, Question


# Create your views here.

def list_all_quiz(request):
    quiz_data = Quiz.objects.all()
    context = {
        'quiz_data':quiz_data
    }
    return render(request, 'quiz/home.html', context=context)

def list_of_quiz_questions(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    quiz_questions = Question.objects.filter(quiz=quiz_id)
    # for question in  quiz_questions:
    #     answer = Answer.objects.get(question=question.id)
    #     print(answer)
    # print( quiz_questions)
    context = {
    'quiz_questions':quiz_questions,
    'quiz_title':quiz.title,
    }

    return render(request, 'quiz/question.html',context=context)

