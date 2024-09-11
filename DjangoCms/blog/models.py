from django.db import models
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateTimeField()
    status = models.CharField(max_length=50, default="Draft")
    date_created = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class PostCategory(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Added on_delete
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Added on_delete

    def __str__(self):
        return f"{self.post.title} - {self.category.name}"
