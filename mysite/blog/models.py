from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.urls import reverse  # 다시 되돌아가기

=======
from django.urls import reverse, reverse_lazy #다시 되돌아가기
>>>>>>> f94a81f13bd7c43718db3fa3f21787a8696e46f5

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_media/', blank=True, null=True)
    video = models.FileField(upload_to='post_media/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})  # 해당 포스트(primary key)로 리버스

<<<<<<< HEAD
    # class Meta:
    #     ordering = ['-published_at']
=======


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="VISITOR")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    class Meta:
        ordering=["-created_at"]
>>>>>>> f94a81f13bd7c43718db3fa3f21787a8696e46f5
