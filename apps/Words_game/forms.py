from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'

        widgets = {
            'qid': forms.DateInput(attrs={'type': 'hidden'}),
        }