from django.shortcuts import render
from .models import Post

def blog_list(request):
    posts = Post.objects.filter(status="Published").order_by('-date_published')[:5]
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/blog_detail.html', {'post': post})