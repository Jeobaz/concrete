from django.contrib import sitemaps
from django.urls import reverse
from datetime import datetime

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'monthly'
    lastmod = datetime(2020,6,17)

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)