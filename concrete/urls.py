from django.contrib import admin
from django.urls import path, include
from concrete import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('create/', views.createGallery, name='createGallery'),
]