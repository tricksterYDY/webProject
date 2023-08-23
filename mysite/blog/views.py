from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import CommentForm
from django.utils import timezone


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

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'   #삭제하면 홈페이지로 다시 redirect

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

# ============ 댓글 ==============
#

def add_comment(request,pk):
    object = Post.objects.get(id=pk)
    if request.method == 'POST':
        form=CommentForm(request.POST, instance=object)
        if form.is_valid():
            name=form.cleaned_data['name']
            content=form.cleaned_data['content']
            c = Comment(post=object, name=name,content=content,created_at=timezone.now)
            c.save()
            return redirect('post-detail',pk=pk)
    else :
        form=CommentForm()
    return render(request,'blog/add_comment.html',{'form':form})

# class CommentCreateView(LoginRequiredMixin, CreateView):
#     model = Comment
#     fields = ['content',]
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         form.instance_post_id = self.kwargs['post_id']
#         return super().form_valid(form)
#
# class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Comment
#     fields = ['content',]
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         form.instance_post_id = self.kwargs['post_id']
#         return super().form_valid(form)
#     def test_func(self):
#         comment=self.get_object()
#         if self.request.user == comment.author: # 현재 로그인한 유저가 포스팅 유저와 같다면..
#             return True
#         return False
#
# class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Comment
#     success_url = reverse_lazy('post-detail')
#
#     def test_func(self):
#         post=self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False
