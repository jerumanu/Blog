from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title=models.CharField(max_length=100)
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )

    updated_on = models.DateTimeField(auto_now= True)
    blog= models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
   

    def publish(self):
        self.updated_on= timezone.now()
        self.save()

    



   


