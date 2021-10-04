from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default="defualt.jpeg",upload_to='pics')
    def __str__(self):
        return f'profle of {self.user}'