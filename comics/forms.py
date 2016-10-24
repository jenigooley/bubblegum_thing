from django import forms

class NewComicForm(forms.Form):
    series = forms.CharField(label='series', max_length=100)
    issue_title = forms.CharField(label='issue title', max_length=200)
    issue_number = forms.CharField(label='issue number', max_length=4)
