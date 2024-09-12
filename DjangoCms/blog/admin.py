from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Post, Category, PostCategory

@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'content')}),
        ('Additional Information', {'fields': ('status', 'date_end')}),
    )
    list_display = ('title', 'date_published', 'date_end', 'status', 'views')
    search_fields = ('translations__title',) 
    list_filter = ('status', 'date_published')

@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['post', 'category']