from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Post, Category, PostCategory
from .forms import CombinedPostCategoryForm

class CategoryListFilter(admin.SimpleListFilter):
    title = 'Categories'
    parameter_name = 'categories'

    def lookups(self, request, model_admin):
        categories = Category.objects.all()
        return [(cat.id, cat.safe_translation_getter('name', any_language=True)) for cat in categories]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(postcategory__category_id=self.value())
        return queryset

class PostAdmin(TranslatableAdmin):
    form = CombinedPostCategoryForm
    list_display = ('get_title', 'status', 'date_end', 'date_published', 'views')
    list_filter = (CategoryListFilter, 'status', 'date_end')
    search_fields = ('translations__title', 'status')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form

    def save_model(self, request, obj, form, change):
        form.save()

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)
    get_title.short_description = 'Title'

class CategoryAdmin(TranslatableAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['post', 'category']

# Register models in admin
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

