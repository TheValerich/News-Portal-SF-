from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        choice = 'NW'
        fields = ['author', 'choice', 'categories', 'title_post', 'text_post', 'rating_post']
