from django import forms
from .models import Solution, Comment

class SolutionForm(forms.ModelForm):
    class Meta:
        model = Solution
        fields = ['title', 'content', 'img']#writer넣어야함

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
