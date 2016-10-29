from django import forms

class NewComicForm(forms.Form):
    series = forms.CharField(label='series', max_length=100)
    issue_title = forms.CharField(label='issue title', max_length=200)
    first_issue = forms.IntegerField(label='first issue number')
    last_issue = forms.IntegerField(label='last issue number')
    notes = forms.CharField(label='notes', max_length=1000)
