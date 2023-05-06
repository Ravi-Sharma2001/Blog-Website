from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
 
def posts(request):
    post = Post.objects.all().order_by('Date')
    return render(request,'post.html', {'posts':post})

def post_detail(request, slug):
   # return HttpResponse(slug)
   post = Post.objects.get(Slug= slug)
   return render(request, 'post_detail.html', {'post':post})


@login_required(login_url="/accounts/login/")
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('Post:list')
        
    else:    
        form = forms.CreatePost()
    return render(request, 'post_create.html',{'form':form})

# Create your views here.
