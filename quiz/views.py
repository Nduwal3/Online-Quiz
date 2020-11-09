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
    if request.method == 'POST':
        quiz_participant_form = QuizParticipantForm(request.POST)
        question_answer_form = QuestionAnswerForm(request.POST)
        if quiz_participant_form.is_valid() and question_answer_form.is_valid():
            print(quiz_participant_form.cleaned_data)
            print(question_answer_form .cleaned_data)
            quiz_participant_form.save()
            return HttpResponse("ok")
        else:
            # return HttpResponse('error')
             return render(request, 'quiz/question.html',{'quiz_participant_form':quiz_participant_form,
        'question_answer_form':question_answer_form})
    else:        
        # create  instance of form
        quiz_participant_form = QuizParticipantForm()
        question_answer_form = QuestionAnswerForm()
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        quiz_questions = Question.objects.filter(quiz=quiz_id)
        context = {
        'quiz_questions':quiz_questions,
        'quiz_title':quiz.title,
        'quiz_participant_form':quiz_participant_form,
        'question_answer_form':question_answer_form
        }

        return render(request, 'quiz/question.html',context=context)




# def result(request):
#             score =0
#             for i in range(len(lst)):
#                 if lst[i]==anslist[i]:
#                     score +=1
#             return render(request,'result.html',{'score':score,'lst':lst})
#         def save_ans(request):
#             ans = request.GET['ans']
#             lst.append(ans)
#         def welcome(request):
#             lst.clear()
#             return render(request,'welcome.html')