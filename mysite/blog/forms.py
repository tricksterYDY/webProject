from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta: #key-value
        model = Post
        fields = ['title', 'content', 'published_at', 'author'] #key