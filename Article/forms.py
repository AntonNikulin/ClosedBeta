from django import forms
from .models import Article

class ArticleAddForm(forms.Form):
    title = forms.CharField(required=True)
    body = forms.Textarea(required=True)
    tags = forms.CharField()