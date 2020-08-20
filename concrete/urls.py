from django.contrib import admin
from django.urls import path, include
from concrete import views
from django.views.generic.base import TemplateView
from django.templatetags.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap



sitemaps = {
    "static": StaticViewSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('send/', views.send, name='send'),
    path('create/', views.createGallery, name='createGallery'),
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path("sitemap.xml/", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]