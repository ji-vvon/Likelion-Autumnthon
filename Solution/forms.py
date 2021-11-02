from django import forms
from .models import Book, Comment, Message

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'content', 'img']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
