from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import MajorBook
from .forms import BookForm

def main(request):
    return render(request, 'main.html')

# 책 목록 페이지
def book_list(request):
    books = MajorBook.objects.all().order_by('-pk')
    return render(request, 'rental_main.html', {'books':books})

# 책 상세 페이지
def detail(request, pk):
    book = MajorBook.objects.get(pk=pk)
    return render(request, 'rental_detail.html', {'book':book})

def new(request):
    if request.method == 'POST': #폼 다채우고 저장버튼 눌렀을 때
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('detail', post.id)
        return redirect('book_list')
    else:  #글을 쓰기위해 들어갔을 때
        form = BookForm()
        return render(request,'rental_new.html', {'form':form})

# 수정
def edit(request, pk):
    edit_book = MajorBook.objects.get(pk=pk)
    return render(request, 'rental_edit.html', {'book':edit_book})

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