from django.contrib import admin
from .models import Post, Category
from parler.admin import TranslatableAdmin

@admin.register(Post)
class PostAdmin(TranslatableAdmin):
    fieldsets = (
        (None, {'fields': ('title', 'content')}),
        ('Additional Information', {'fields': ('status', 'date_end')}),
    )
    list_display = ('title', 'date_published', 'status', 'views')
    search_fields = ('translations__title',) 
    list_filter = ('status', 'date_published')

# Register the Category model
@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('name',)
    search_fields = ('translations__name',)
