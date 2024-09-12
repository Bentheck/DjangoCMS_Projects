from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_detail(request, id):
    post = get_object_or_404(Post, pk=id) 
    if post.status == "Published":
        post.views += 1
        post.save(update_fields=['views'])
    return render(request, 'blog/blog_detail.html', {'post': post})

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog_list.html', {'posts': posts})