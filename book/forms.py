from django import forms
from .models import MajorBook

class BookForm(forms.ModelForm):
    class Meta:
        model = MajorBook
        fields = ['title', 'author', 'publisher', 'category', 'img', 'info_text', 'status']