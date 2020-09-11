from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle=models.CharField(max_length=80,null=True, blank=True)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'The is {self.title} written by {self.author}'
