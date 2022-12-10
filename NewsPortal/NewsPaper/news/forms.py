import requests
from django.forms import ModelForm, ModelMultipleChoiceField, HiddenInput
from django.http import request
from django_filters import ModelChoiceFilter

from .models import Post, Category, Author



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            # 'author',
            'categoryType',
            'title',
            'text',
            'postCategory',
            ]
        # exclude = ('author',)

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ]
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            'authorUser'
        ]