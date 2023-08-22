from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Post
from .forms import PostForm

from django.contrib.auth.decorators import login_required

# Create your views here.

def about(request):
    posts=Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'blog/about.html', context)

def web01(request):
    return HttpResponse('<h1> Web01 page </h1>')

def web02(request):
    return HttpResponse('<h1> Web02 page </h1>')

#====================================

@login_required
def create_post(request):
    if request.method=='GET':
        context={'form':PostForm()}
        return render(request, 'blog/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')    #path('', views.home, name="posts"),
        else:
            return redirect(request,'blog/post_form.html', {'form':form})
        
#====================================

@login_required
def edit_post(request,id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset,id=id)
    
    # post=get_object_or_404(Post, id=id) #원본 : URL 패턴과 일치하지 않으면 404로 리턴
    if request.method=='GET':   # get : http://127.0.0.1:8000/post/edit/1
        context={'form': PostForm(instance=post),'id':id}
        return render(request,'blog/post_form.html',context)
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'The post has been updated successfully.')
            return redirect('posts')
        else:
            messages.error(request,'Please correct the following errors:')
            return render(request,'blog/post_form.html',{'form':form})
            
            
@login_required    
def delete_post(request,id):
    queryset = Post.objects.filter(author=request.user)
    post=get_object_or_404(queryset,id=id)
    # post=get_object_or_404(Post,id=id)
    context={'post':post}
    if request.method == 'GET': # get : http://127.0.0.1:8000/post/delete/1
        return render(request,'blog/post_confirm_delete.html',context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,'The post has been deleted successfully.')
        return redirect('posts')

