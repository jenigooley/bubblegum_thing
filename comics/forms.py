from django import forms
from .models import Comic


class NewComicForm(forms.ModelForm):

    first_issue = forms.IntegerField(label='first issue number')
    last_issue = forms.IntegerField(label='last issue number')

    class Meta:
        fields = ['series', 'issue_title', 'notes']
        model = Comic
