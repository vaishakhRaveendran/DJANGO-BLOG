from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    #Users and posts are having a one to many relationship....
    author=models.ForeignKey(User,on_delete=models.CASCADE)

