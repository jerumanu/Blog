from django.db import models



class Post(models.Model):
    title=models.CharField(max_length=50)
    blog =models.CharField(max_length=400 )
    # author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    name= models.CharField(max_length=50)   



   


