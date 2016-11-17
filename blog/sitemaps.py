from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSiteMap(Sitemap):
    freq = 'weekly'
    priority = 0.3

    def items(self):
        return Post.published.all()

    def lastmod(self, obj):
        return obj.publish