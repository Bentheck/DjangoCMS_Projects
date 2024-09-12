from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from models import Post

class Command(BaseCommand):
    help = 'Check and update a variable daily'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        # Example logic: Update a field or perform an operation
        Post.objects.filter(status="Published", date_end__lt=now).update(status="Archived")
        