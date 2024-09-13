from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CombinedPostCategoryForm

class PostCreatePlugin(CMSPluginBase):
    model = CMSPlugin  # Using CMSPlugin as a placeholder model
    name = _("Create Post")
    render_template = "blog/plugins/create_post_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        request = context['request']
        if request.method == "POST":
            form = CombinedPostCategoryForm(request.POST)
            if form.is_valid():
                # Save the new post and get the instance
                new_post = form.save()
                # Redirect to the detail page of the newly created post
                return redirect(reverse('blog:blog_detail', args=[new_post.id]))
        else:
            form = CombinedPostCategoryForm()

        context.update({
            'form': form,
        })
        return context

plugin_pool.register_plugin(PostCreatePlugin)