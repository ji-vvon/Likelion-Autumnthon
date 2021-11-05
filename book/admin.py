from django.contrib import admin
from .models import MajorBook, BorrowedBook
# Register your models here.

admin.site.register(MajorBook)
admin.site.register(BorrowedBook)