from django import forms

from .models import Blog

class NewBlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 100, 'rows': 30}),
        }
