from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils import timezone

import logging

logger = logging.getLogger(__name__)


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
    date_end = models.DateTimeField(null=True, blank=True, verbose_name="Archival Date")
    views = models.IntegerField(default=0, editable=False)

    # Override the save method to set the date_published field
    def save(self, *args, **kwargs):
        if self.status == "Published" and not self.date_published:
            self.date_published = timezone.now()
        
        super().save(*args, **kwargs)


    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)


class Category(TranslatableModel):
    id = models.AutoField(primary_key=True)
    
    translations = TranslatedFields(
        name=models.CharField(max_length=255, blank=False, null=False),
        description=models.TextField()
    )

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post', 'category')
        constraints = [
            models.UniqueConstraint(fields=['post', 'category'], name='unique_post_category')
        ]

    def __str__(self):
        return f"{self.post.safe_translation_getter('title', any_language=True)} - {self.category.safe_translation_getter('name', any_language=True)}"
