from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=True)
