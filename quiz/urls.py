from django.urls import path
from .views import list_all_quiz, list_of_quiz_questions

urlpatterns = [
    # quiz/all/
    path('all/', list_all_quiz),
    path('<int:quiz_id>/questions/', list_of_quiz_questions),
]