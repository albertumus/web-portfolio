from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog/<int:entrada_de_blog_id>/<slug:entrada_de_blog_slug>/' , views.entrada_de_blog, name="entrada de blog"),
    path('category/<int:category_id>/', views.entrada_de_blog_category, name="categoria de blog" ),
]
