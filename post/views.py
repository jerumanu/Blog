from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
 
# Views


def index(request):
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





def upload(request):
    upload = PostCreate()
    if request.method == 'POST':
        upload = PostCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'post/upload_form.html', {'upload_form':upload})



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
    return render(request, 'post/upload_form.html', {'upload_form':post_form})


def delete_post(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Post.objects.get(id = post_id)
    except Post.DoesNotExist:
        return redirect('index')
    post_sel.delete()
    return redirect('index')
