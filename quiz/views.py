from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Quiz, Question

from .forms import  QuizParticipantForm, QuestionAnswerForm


# Create your views here.

def list_all_quiz(request):
    quiz_data = Quiz.objects.all()
    context = {
        'quiz_data':quiz_data
    }
    return render(request, 'quiz/home.html', context=context)

def list_of_quiz_questions(request, quiz_id):    
    quiz_questions = Question.objects.filter(quiz=quiz_id)
    if request.method == 'POST':
        quiz_participant_form = QuizParticipantForm(request.POST)
        question_answer_form = QuestionAnswerForm(request.POST)
        if quiz_participant_form.is_valid() and question_answer_form.is_valid():
            print(question_answer_form.cleaned_data)
            full_score = len(quiz_questions)
            name = quiz_participant_form.cleaned_data['user']
            form2 = quiz_participant_form.save(commit=False)
            form2.score = 10
            form2.save()
            context = {
            'total_score':10,
            'name':name,
            'full_score':full_score
            }
            return render(request, 'quiz/score.html',context=context)
        else:
            return HttpResponse('error')
    else:        
        # create  instance of form
        quiz_participant_form = QuizParticipantForm()
        question_answer_form = QuestionAnswerForm()        
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        context = {
        'quiz_questions':quiz_questions,
        'quiz_title':quiz.title,
        'quiz_participant_form':quiz_participant_form,
        'question_answer_form':question_answer_form
        }
        return render(request, 'quiz/question.html',context=context)
