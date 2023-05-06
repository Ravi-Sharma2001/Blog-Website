from django import forms
from django.forms import fields
from .import models

class CreatePost(forms.ModelForm):
    class Meta:
        model =models.Post
        fields =['Title', 'Body','Slug','thumb']