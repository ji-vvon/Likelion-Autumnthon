from django import forms
from .models import MajorBook,BorrowedBook

class BookForm(forms.ModelForm):
    class Meta:
        model = MajorBook
        fields = ['title', 'author', 'publisher', 'pub_date', 'category', 'img', 'info_text', 'status']


class BorrowedBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = ['borrower','borrow_book']