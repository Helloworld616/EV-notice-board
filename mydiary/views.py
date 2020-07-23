from django.shortcuts import render, redirect
from .models import Content


def home(request):
    posts = Content.objects.all
    return render(request, 'index.html', {'posts_list':posts})

def index(request):
    return render(request, 'index.html')
