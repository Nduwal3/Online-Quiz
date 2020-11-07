from django.forms import ModelForm

from .models import Answer

class AnswerModelForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['correct_ans']
