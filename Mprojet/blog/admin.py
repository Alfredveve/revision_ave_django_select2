from django.contrib import admin
from . models import BlogArticles

class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','datapub', 'slug', 'slug']

admin.site.register(BlogArticles, BlogArticleAdmin)
