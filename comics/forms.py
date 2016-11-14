from django import forms
from .models import Comic
from django.forms import TextInput

class NewComicForm(forms.ModelForm):

    first_issue = forms.CharField(label='first issue number', widget=forms.TextInput(attrs={'placeholder': 'first issue'}))
    last_issue = forms.CharField(label='last issue number', widget=forms.TextInput(attrs={'placeholder': 'last issue'}))

    class Meta:
        fields = ['series']

        model = Comic
        widgets = {
            'series': TextInput(attrs={'placeholder': 'series'})
        }
# class manuel_comic_entry(forms.ModelForm):
#
#     series = forms.CharField(max_length=200)
#     issue_number = forms.CharField(max_length=4)
#     issue_title = forms.CharField(max_length=200, null=True, blank=True)
#     description = forms.CharField(max_length=200)
#     cover_art = forms.URLField(max_length=500)
#     writer = forms.ForeignKey('People', related_name='writerpeople')
#     artist = forms.ForeignKey('People', related_name='artistpeople')
#     letterer = forms.ForeignKey('People', related_name='lettererpeople')
#     publisher = forms.ForeignKey('Publisher', max_length=200)
#     cover_date = forms.DateField('date published')
#     notes = forms.CharField(max_length=1000, null=True, blank=True)
