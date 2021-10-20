from django.db import models
from django import forms
from django.core import validators
from django.core.validators import ValidationError
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE
from tinymce.models import HTMLField


# Create your models here.
def min_length_check(val):
    if len(val) <= 10:
        raise ValidationError("%(val)s Must be Greater then 10", params={'val': val})


class Category(models.Model):
    title = models.CharField(validators=[min_length_check], max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager

    def __str__(self):
        return self.title

    def natural_key(self):
        return [self.id, self.title, self.created_at]

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created_at']


class Posts(models.Model):
    title = models.CharField(validators=[min_length_check], max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    thumbnail = models.FileField(upload_to='posts/', null=True)
    category = models.ManyToManyField(Category, default=0)
    content = HTMLField(validators=[min_length_check])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'thumbnail', 'user', 'category']
        widgets ={
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Post Tiltle'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control', 'multiple': True}),
            'content': TinyMCE(attrs={'class': 'form-control'}),
            'user':  forms.Select(attrs={'class': 'form-control'}),
            'category': forms.CheckboxSelectMultiple(attrs={'class': 'list-unstyled list-inline'}),
        }
        help_text={
            'title': 'Enter Title Here',
        }
        error_messages ={}
        labels={
            'title': 'Enter Post Title',
        }
    def clean(self):
        fields = self.cleaned_data
        keys = list(fields.keys())
        print(fields)
        if(len(fields['title']) <=10):
            raise ValidationError("%(val)s Must be Greater then 10", params={'val': keys[0]})
        if (len(fields['content']) <= 10):
            raise ValidationError("%(val)s Must be Greater then 10", params={'val': keys[1]})


class Gallery(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    images = models.FileField(upload_to="posts/", blank=True, null=True)