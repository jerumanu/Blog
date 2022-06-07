from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title=models.CharField(max_length=50)
    
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    blog= models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
   



   


