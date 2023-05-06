
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    Title = models.CharField(max_length=100)
    Slug = models.SlugField()
    Body = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default= 'hi.jpg', blank= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=None)


    def __str__(self):
        return self.Title
    def snippet(self):
        return self.Body[:50] + "..."