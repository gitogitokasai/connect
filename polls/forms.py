from django import forms
from .models import Question, Choice


class TestForm(forms.Form):
    test_text = forms.CharField(max_length=100)
    aho_text = "しょうもないね"


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ('name', 'choice_text','question')
