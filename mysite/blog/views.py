from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


def about(request):
    # posts=Post.objects.all()
    # context = {'posts' : posts}
    return render(request, 'blog/me_profile.html')

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

#====================================
class PostListView(ListView):
    model=Post
    template_name = "blog/home.html"   # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ['-published_at']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form): #Post 눌렀을 때 제대로 올라가기 위해서..
        form.instance.author = self.request.user    #쓰는사람 현재 유저야!
        return super().form_valid(form) #부모 클래스로 전달
    # 이것만 하면 define a get_absolute_url method on the Model. 오류 발생 -> Model.py

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author: # 현재 로그인한 유저가 포스팅 유저와 같다면..
            return True
        return False

class PostDeleteVie(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'   #삭제하면 홈페이지로 다시 redirect

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

