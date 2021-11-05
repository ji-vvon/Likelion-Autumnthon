from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from .models import MajorBook, BorrowedBook
from .forms import BookForm, BorrowedBookForm
from django.contrib import messages
from solution.models import Solution#솔루션 책의 데이터
from django.contrib.auth.forms import UserChangeForm

def main(request):
    b = MajorBook.objects.all().order_by('-id')
    book_paginator = Paginator(b, 4)
    book = request.GET.get('page')
    books = book_paginator.get_page(book)

    s = Solution.objects.all().order_by('-id')
    solution_paginator = Paginator(s, 4)
    # solution = request.GET.get('page')
    solutions = solution_paginator.get_page(book)

    contents = Solution.objects.all().order_by('-id')
    return render(request, 'main.html', {'books' : books, 'solutions' : solutions,'contents' : contents})

# 책 목록 페이지
def book_list(request):
    books = MajorBook.objects.all().order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request, 'rental_main.html', {'books' : books, 'posts' : posts})

# 내가 등록한 책 목록
def mybook(request):
    me = request.user
    books = MajorBook.objects.all().filter(uploader=me).order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request, 'mybook.html', {'books': books, 'posts':posts})


# 책 상세 페이지
def detail(request, pk):
    book = MajorBook.objects.get(pk=pk)
    return render(request, 'rental_detail.html', {'book':book})

def new(request):
    if request.method == 'POST': #폼 다채우고 저장버튼 눌렀을 때
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.upload_date = timezone.now()
            post.uploader = request.user
            post.save()    
        user=UserChangeForm(instance = request.user).save(commit=False)#대여시 코인을 차감해줍니다
        if user.coin:
            if user.coin>0:
                user.coin+=3
                user.save()
            return redirect('detail', post.id)
        return redirect('book_list')
    else:  #글을 쓰기위해 들어갔을 때
        form = BookForm()
        return render(request,'rental_new.html', {'form':form})

# 수정
def edit(request, pk):
    edit_book = MajorBook.objects.get(pk=pk)
    return render(request, 'rental_edit.html', {'book':edit_book})

# 수정이 안되는 오류 발생
def update(request, pk):
    update_book = MajorBook.objects.get(pk=pk)
    update_book.title = request.POST['title']
    update_book.author = request.POST['author']
    update_book.publisher = request.POST['publisher']
    update_book.pub_date = request.POST['pub_date']
    update_book.upload_date = timezone.now()
    update_book.info_text = request.POST['info_text']
    update_book.status = request.POST['status']
    update_book.save()
    return redirect('detail', update_book.pk)

# 삭제
def delete(request, pk):
    delete_book = MajorBook.objects.get(pk=pk)
    delete_book.delete()
    return redirect('book_list')

def rental(request, id):
    rental_book = MajorBook.objects.get(pk=id)
    rental_status=rental_book.status #대여여부
    
    if rental_status == '대여 가능':
        user=UserChangeForm(instance = request.user).save(commit=False)#대여시 코인을 차감해줍니다
        if user.coin:
            if user.coin>0:
                user.coin-=1
                user.save()

                rental_book.status = '대여중'
                rental_book.save()
                messages.success(request, '대여가 성공했습니다!')

                form=BorrowedBookForm().save(commit=False) #여기부터는 내가 빌린 책 기능을 위해 데이터를 넘겨주는 부분입니다.
                form.borrower=request.user #로그인 된 유저를 빌린이에 추가합니다
                form.borrow_book=rental_book#책을 외래키로 저장합니다
                BorrowedBook=form.save()          
        else:
            messages.success(request, '코인이 부족합니다!')


        return redirect('book_list')
    # else:
    #     messages.success(request, '대여가 불가능한 책입니다!')
    #     return redirect('book_list')

# 마이페이지
def mypage(request):
    me = request.user
    books = MajorBook.objects.all().filter(uploader=me).order_by('-id')
    borrowed_books = BorrowedBook.objects.all().filter(borrower=me).order_by('-id')
    return render(request, 'mypage.html', {'books': books,
                                            'borrowed_books':borrowed_books,
                                            })

def category_IT(request):
    category = 'IT'
    books = MajorBook.objects.all().filter(category='IT').order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request, 'rental_main.html', {'books' : books, 'posts' : posts, 'category': category})

def category_society(request):
    category = '사회'
    books = MajorBook.objects.all().filter(category='사회').order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request, 'rental_main.html', {'books' : books, 'posts' : posts, 'category': category})

def category_science(request):
    category = '과학'
    books = MajorBook.objects.all().filter(category='과학').order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request, 'rental_main.html', {'books' : books, 'posts' : posts, 'category': category})

def category_art(request):
    category = '예술'
    books = MajorBook.objects.all().filter(category='예술').order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request, 'rental_main.html', {'books' : books, 'posts' : posts, 'category': category})

def category_etc(request):
    category = '기타'
    books = MajorBook.objects.all().filter(category='기타').order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request, 'rental_main.html', {'books' : books, 'posts' : posts, 'category': category})


def myborrowed_book(request):
    me = request.user
    books = BorrowedBook.objects.all().filter(borrower=me).order_by('-id')
    paginator = Paginator(books, 8)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request, 'myborrowed_book.html', {'books': books, 'posts':posts})

# 검색
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']        
        books = MajorBook.objects.filter(title__contains=searched)
        paginator = Paginator(books, 8)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, 'searched.html', {'searched': searched, 'books': books, 'posts':posts})
    else:
        return render(request, 'searched.html')

#placeholder
def placeholder(request):
    return render(request, 'placeholder.html', {})