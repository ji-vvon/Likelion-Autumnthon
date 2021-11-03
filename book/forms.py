from django import forms
from .models import MajorBook

class BookForm(forms.ModelForm):
    class Meta:
        model = MajorBook
        fields = ['title', 'author', 'publisher', 'pub_date', 'category', 'img', 'info_text', 'status']


# class BorrowForm(forms.ModelForm):
#     class Meta:
#         model = BorrowBook
#         fields = ['title', 'author', 'publisher', 'pub_date', 'category']