from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

def main(request):
    return render(request, 'main.html')

def write(request):
    if (request.method == 'POST'):
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
                form = form.save(commit=False)
                form.pub_date = timezone.now()
                form.save()
                return redirect('main')
    else:
            form = PostForm()
            return render(request, 'write.html' ,{'form':form})

def read(request):
    obj = Post.objects
    return render(request, 'read.html' , {'obj':obj})
def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detail.html', {'post' :post})
def edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES , instance = post)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('read')
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html' , {'form' : form})
def delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('read')