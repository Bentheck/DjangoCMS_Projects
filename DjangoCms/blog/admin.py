from django.contrib import admin
from .models import Post, Category

# Register the Post model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    search_fields = ('title', 'content')

# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
