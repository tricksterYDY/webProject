from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse  # 다시 되돌아가기


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

    # class Meta:
    #     ordering = ['-published_at']
