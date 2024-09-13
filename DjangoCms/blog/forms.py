from django import forms
from .models import Post, Category, PostCategory
from django.utils import timezone

class CombinedPostCategoryForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter post title'
        })
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={  # Changed to standard Textarea widget
            'class': 'form-control',
            'placeholder': 'Enter post content',
            'rows': 5  # Adjust rows as needed
        })
    )
    status = forms.ChoiceField(
        choices=Post._meta.get_field('status').choices,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    date_end = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Select end date',
            'type': 'datetime-local'
        })
    )
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'date_end', 'categories']

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
            # Link the post with the selected categories
            PostCategory.objects.filter(post=post).delete()  # Clear previous links
            categories = self.cleaned_data.get('categories')
            for category in categories:
                PostCategory.objects.get_or_create(post=post, category=category)
        return post

    def clean_date_end(self):
        date_end = self.cleaned_data.get('date_end')
        if date_end and date_end < timezone.now():
            raise forms.ValidationError("The end date cannot be in the past.")
        return date_end
