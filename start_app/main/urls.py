from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog-register/', views.blog_register, name='blog_register'),
]

