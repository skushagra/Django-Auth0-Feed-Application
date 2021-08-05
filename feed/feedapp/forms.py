from django.forms import ModelForm, TextInput, widgets
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        widgets = {
            'text': TextInput(attrs=({'class' : 'input', 'placeholder': 'Say something...'}))
        }