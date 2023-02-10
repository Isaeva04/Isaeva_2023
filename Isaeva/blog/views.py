from django.shortcuts import render
from .models import Post

def blog(request):
    return render(request,'blog.html')

def blog_index(request):
    blog = Post.objects.all()
    context = {
        'blog': blog
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    blog = Post.objects.get(pk=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blog_detail.html', context)
