from django.forms import ModelForm

from .models import QuizParticipant, Question

class QuizParticipantForm(ModelForm):
    class Meta:
        model = QuizParticipant
        fields = ['user']
    
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