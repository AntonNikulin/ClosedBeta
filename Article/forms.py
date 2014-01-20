from django import forms
from .models import Article

class ArticleAddForm(forms.Form):
    Title = forms.CharField(required=True)
    Body = forms.CharField(widget=forms.Textarea)
    tags = forms.CharField()