from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import gettext_lazy as _

class BlogApp(CMSApp):
    app_name = "blog"  # App namespace
    name = _("Blog Application")  # Name of the app

    def get_urls(self, page=None, language=None, **kwargs):
        return ["blog.urls"]  # Hook into the app's URLs

apphook_pool.register(BlogApp)  # Register the app