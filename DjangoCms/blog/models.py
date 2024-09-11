from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils import timezone

class Post(TranslatableModel):
    id = models.AutoField(primary_key=True)
    date_published = models.DateTimeField(null=True, blank=True, editable=False)

    translations = TranslatedFields(
        title=models.CharField(max_length=255),
        content=models.TextField()
    )

    status = models.CharField(
        max_length=50,
        default="Draft",
        choices=[
            ("Draft", "Draft"),
            ("Published", "Published"),
            ("Archived", "Archived")
        ]
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(null=True, blank=True, verbose_name="Archival Date (Leave empty for no auto-archiving)")
    views = models.IntegerField(default=0, editable=False)

    def save(self, *args, **kwargs):
        if self.status == "Published" and not self.date_published:
            self.date_published = timezone.now()
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(TranslatableModel):
    id = models.AutoField(primary_key=True)

    translations = TranslatedFields(
        name=models.CharField(max_length=255),
        description=models.TextField()
    )

    def __str__(self):
        return self.name

class PostCategory(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.post.title} - {self.category.name}"
