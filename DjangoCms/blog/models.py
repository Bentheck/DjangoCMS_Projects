from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default="Draft" , choices=[("Draft", _("Draft")), ("Published", _("Published")), ("Archived", _("Archived"))])
    date_created = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0, auto_created=True)

    def save(self, *args, **kwargs):
        # Check if the status is changing to "Published" and the date_published is not set. So once set, it won't change.
        if self.status == "Published" and not self.date_published:
            self.date_published = timezone.now()

            super().save(*args, **kwargs)

    def __str__(self):
        return self.title

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
