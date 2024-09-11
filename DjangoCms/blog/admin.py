from django.contrib import admin
from .models import Post, Category
from parler.admin import TranslatableAdmin

# Register the Post model
@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    list_display = ('title', 'status')
    search_fields = ('title', 'content')

# Register the Category model
@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name',)
    search_fields = ('name',)