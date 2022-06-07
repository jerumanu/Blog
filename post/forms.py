from django import forms


from .models import *
#DataFlair



class PostCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'