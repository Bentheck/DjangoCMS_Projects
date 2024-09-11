from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import gettext_lazy as _

class BlogApp(CMSApp):
    app_name = "blog"
    name = _("Blog Application")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["blog.urls"] 

apphook_pool.register(BlogApp)