from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponse



def index(request):
    post = Post.objects.all()
    return render(request, 'post/blog.html', {'post': post})


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
