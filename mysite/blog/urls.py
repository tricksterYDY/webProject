"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
<<<<<<< HEAD

urlpatterns = [
    path('', views.PostListView.as_view(), name="home"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name="post-detail"),
    path('my_posts', views.about, name="posts"),
    path('post/create', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name="post-edit"),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name="post-delete"),
    path('api/posts/', views.PostList.as_view(), name='post-list'),
    path('api/posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
]
=======
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView)

urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('my_posts',views.about, name="posts"),
    path('post/create',PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name="post-edit"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="post-delete"),
    path('post/<int:pk>/add_comment', views.add_comment, name="add-comment"),

    # path('post/<int:post_id>/comment/create',CommentCreateView.as_view(), name='comment-create'),
    # path('comment/<int:pk>/update', CommentUpdateView.as_view(), name="comment-edit"),
    # path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name="comment-delete")

]
>>>>>>> f94a81f13bd7c43718db3fa3f21787a8696e46f5
