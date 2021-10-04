from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(default=timezone.now)
    content=models.TextField()
    def __str__(self):
        return f'post of {self.author.username}'

        
    def get_absolute_url(self):
        return reverse('datail-post',kwargs={'pk': self.pk})