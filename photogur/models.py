from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    user = models.ForeignKey(User, default = 1, on_delete=models.CASCADE, related_name='picture')

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE, related_name='comments')
    