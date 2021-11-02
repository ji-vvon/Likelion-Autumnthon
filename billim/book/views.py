from django.shortcuts import render, redirect
from django.utils import timezone
from .models import MajorBook
from .forms import BookForm

# 책 목록 페이지
def book_list(request):
    books = MajorBook.objects.all().order_by('-pk')
    return render(request, 'list.html', {'books':books})

# 책 상세 페이지
def detail(request, pk):
    book = MajorBook.objects.get(pk=pk)
    return render(request, 'detail.html', {'book':book})

# 책 등록 페이지
def new(request):
    form = BookForm()
    return render(request, 'new.html', {'form':form})

# 책 저장
def create(request):  
    form = BookForm(request.POST, request.FILES)
    if form.is_valid():
        new_book = form.save(commit=False)
        new_book.save()
        return redirect('detail', new_book.id)
    return redirect('detail')

# 수정
def edit(request, pk):
    edit_book = MajorBook.objects.get(pk=pk)
    return render(request, 'edit.html', {'book':edit_book})

def update(request, pk):
    update_book = MajorBook.objects.get(pk=pk)
    update_book.title = request.POST['title']
    update_book.author = request.POST['author']
    update_book.publisher = request.POST['publisher']
    update_book.pub_date = request.POST['pub_date']
    update_book.info_text = request.POST['info_text']
    update_book.status = request.POST['status']
    update_book.save()
    return redirect('detail', update_book.pk)

def delete(request, pk):
    delete_book = MajorBook.objects.get(pk=pk)
    delete_book.delete()
    return redirect('book_list')