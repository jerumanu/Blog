from django import forms


from .models import *
#DataFlair



class PostCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'blog',)

    widget = {
        'title':forms.TextInput(attrs={'class':'form control' }),
        'blog':forms.Textarea(attrs={'class':'form control' })
    }    