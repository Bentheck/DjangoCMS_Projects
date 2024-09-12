from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

def blog_detail(request, id):
    post = get_object_or_404(Post, pk=id) 
    now = timezone.now()

    # Archive post if date_end is in the past
    if post.date_end and post.date_end < now:
        post.status = "Archived"
        post.save(update_fields=['status'])    

    # Increase views if the post is still published
    if post.status == "Published":
        post.views += 1
        post.save(update_fields=['views'])

    # If the post is archived, render the archived template
    if post.status == "Archived":
        return blog_archived(request, post)

    return render(request, 'blog/blog_detail.html', {'post': post})


def blog_list(request):
    now = timezone.now()

    # Archive posts where date_end is in the past
    Post.objects.filter(status="Published", date_end__lt=now).update(status="Archived")

    # Get published posts
    posts = Post.objects.filter(status="Published")

    return render(request, 'blog/blog_list.html', {'posts': posts})


def blog_archived(request, post):
    return render(request, 'blog/blog_archived.html', {'post': post})