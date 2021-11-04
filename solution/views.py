from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from .models import Solution, Comment
from .forms import SolutionForm, CommentForm
from datetime import date, datetime
from django.conf import settings
from django.shortcuts import render

def solution_home(request):
    contents = Solution.objects.all().order_by('-id')
    paginator = Paginator(contents, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request,'solution_main.html', {'contents' : contents, 'posts' : posts})

def solution_detail(request, id):
    detail_data = get_object_or_404(Solution, pk = id)
    comments = Comment.objects.filter(solution_id=id, comment_id__isnull=True)

    re_comments = []
    for comment in comments:
        re_comments += list(Comment.objects.filter(comment_id=comment.id))
    
    form = CommentForm()
    return render(request, 'solution_detail.html' ,{'data' : detail_data, 'comments' : comments, 're_comments' : re_comments, 'form':form})

def solution_new(request):
    if request.method == 'POST': #폼 다채우고 저장버튼 눌렀을 때
        form = SolutionForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.writer = request.user
            post.pub_date = timezone.now() #날짜 생성
            post.save()
            return redirect('solution_detail', post.id)
        return redirect('home')
    else:  #글을 쓰기위해 들어갔을 때
        form = SolutionForm()
        return render(request,'solution_write.html', {'form':form})

def solution_update(request, id):
    post = get_object_or_404(Solution, pk = id)
    if request.method == 'GET':  #수정하려고 들어갔을 때
        form = SolutionForm(instance = post)
        return render(request, 'solution_update.html', {'form' : form})
    else:   #수정 끝나고 수정 버튼을 눌렀을 때
        form = SolutionForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('/solution/solution_detail/' + str(id))
        return redirect('/solution')

def solution_delete(request, id):
    delete_data =  Solution.objects.get(id = id)
    delete_data.delete()
    return redirect('/solution')

def solution_search(request):
    data = Solution.objects.all().order_by('-id')

    find = request.POST.get('find', "")

    if find:
        data = data.filter(title__icontains=find)
        return render(request, 'search.html', {'data': data, 'find':find})
    else:
        return render(request, 'search.html')

def create_comment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.solution_id = Solution.objects.get(pk=id)
            comment.writer = request.user
            comment.save()
    return redirect('solution_detail', id)

def create_re_comment(request, id, comment_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.solution_id = Solution.objects.get(pk=id)
            comment.comment_id = Comment.objects.get(pk=comment_id)
            comment.writer = request.user
            comment.save()
    return redirect('solution_detail', id)

def update_comment(request, comment_id, id):
    my_com = Comment.objects.get(id=comment_id)
    com_form = CommentForm(instance=my_com)
    if request.method == "POST":
        update_form = CommentForm(request.POST, instance = my_com)
        if update_form.is_valid():
            update_form.save()
            return redirect('solution_detail', id)
    return render(request, 'solution_detail', {'com_form':com_form})

def delete_comment(request, comment_id, id):
    mycom = Comment.objects.get(id=comment_id)
    mycom.delete()

    return redirect('solution_detail', id)
