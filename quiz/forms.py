from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import QuizParticipant, Question

class QuizParticipantForm(ModelForm):
    class Meta:
        model = QuizParticipant
        fields = ['user']
        labels = {
            'user': _('Fullname '),
        }
    
    def clean(self):
        super().clean()
        user= self.cleaned_data.get("user")
        if not user:
            raise forms.ValidationError(
                "username is Required"
            )

class QuestionAnswerForm(ModelForm):
    class Meta:
        model = Question
        fields = ['correct_ans']
        labels = {
            'correct_ans': _(''),
        }