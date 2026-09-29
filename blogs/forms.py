from catalog.forms import StyleFromMixin
from django import forms
from django.core.exceptions import ValidationError
from .models import BlogPost
from PIL import Image


class BlogPostForm(StyleFromMixin, forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image',]