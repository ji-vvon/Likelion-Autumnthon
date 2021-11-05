from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib import messages


def notice(request):
    return render(request, 'notice.html', {})

def guide(request):
    return render(request, 'guide.html', {})

def producer(request):
    return render(request, 'producer.html', {})