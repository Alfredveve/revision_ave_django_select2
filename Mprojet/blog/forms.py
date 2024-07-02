from django import forms
from . models import BlogArticles


class BlogArticlesForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'la descripton ici'}))
    class Meta:
        model = BlogArticles
        fields = ['title', 'description', 'image', 'datapub', 'slug']