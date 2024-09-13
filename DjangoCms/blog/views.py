from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, PostCategory
from django.utils import timezone
from .forms import CombinedPostCategoryForm
from django.utils.translation import get_language

def blog_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    categories = Category.objects.filter(postcategory__post=post)
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

    return render(request, 'blog/blog_detail.html', {'post': post, 'categories': categories})

def blog_list(request):
    now = timezone.now()

    # Archive posts where date_end is in the past
    Post.objects.filter(status="Published", date_end__lt=now).update(status="Archived")

    # Get published posts
    posts = Post.objects.filter(status="Published")

    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_archived(request, post):
    return render(request, 'blog/blog_archived.html', {'post': post})

def create_post(request):
    if request.method == "POST":
        form = CombinedPostCategoryForm(request.POST)
        if form.is_valid():
            # Save the new post and get the instance
            new_post = form.save(commit=False)
            # Set the language of the post based on the current request language
            new_post.set_current_language(get_language())
            new_post.save()
            # Redirect to the detail page of the newly created post
            return redirect('blog:blog_detail', id=new_post.id)
    else:
        form = CombinedPostCategoryForm()

    return render(request, 'blog/create_post.html', {'form': form})
