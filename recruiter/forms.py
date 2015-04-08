from django import forms

from .models import Candidate

class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ('name', 'email', 'html', 'css', 'javascript', 'python', 'django', 'ios', 'android')