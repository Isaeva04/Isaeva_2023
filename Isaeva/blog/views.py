from django.shortcuts import render
from .models import Post

# def blog(request):
#     return render(request,'blog.html')

def blog_index(request):
    Posts = Post.objects.all().order_by('-id')  #  в переменную посты выгружаются все объекты БД Пост
    context = {
        'Posts': Posts    # словарь в который загружаются все посты
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    return render(request, 'blog_detail.html', context)
