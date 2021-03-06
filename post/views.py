
from collections import UserList
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
 
# Views


def index(request):
    post = Post.objects.all()
    return render(request, 'post/post.html', {'post': post})

def mypost(request):
    post = Post.objects.all()
    return render(request, 'post/blog.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})





    

@login_required(login_url='/login/')
def upload(request):
    if request.method == "POST":
        form = PostCreate(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostCreate()
    return render(request, 'post/upload_form.html', {'form': form})
  

@login_required(login_url='/login/')
def update_post(request, post_id):
  
    post_id = int(post_id)
    try:
        post_sel = Post.objects.get(id = post_id)
    except Post.DoesNotExist:
        return redirect('index')
    post_form = PostCreate(request.POST or None, instance = post_sel)
    if post_form.is_valid():
       post_form.save()
       return redirect('index')
    
    return render(request, 'post/upload_form.html', {'form': post_form})

@login_required(login_url='/login/')
def delete_post(request,  post_id):
    
    post_sel = int( post_id)
    try:
        post_sel = Post.objects.get(id = post_id)
    except Post.DoesNotExist:
        return redirect('index')
    post_sel.delete()
    return redirect('index')
