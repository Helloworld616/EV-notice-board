from django.shortcuts import render, redirect
from .models import Content
from .models import timezone
from .forms import ContentForm


def index(request):
    posts = Content.objects.all
    return render(request, 'index.html', {'posts_list':posts})


def new(request):
     
     if request.method == 'POST':
         form = ContentForm(request.POSST, request.FILES)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date  = timezone.now()
             post.save()
             return redirect('home')
     else :
        form = ContentForm()
    
     return render(request, 'new.html', {'form':form})