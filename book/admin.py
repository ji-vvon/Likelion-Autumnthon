from django.contrib import admin
from .models import MajorBook, Category, BorrowedBook
# Register your models here.

admin.site.register(MajorBook)
admin.site.register(Category)
admin.site.register(BorrowedBook)