from django.contrib import admin
from .models import BlogPost

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published', 'views_count',)
    list_filter = ('created_at', 'is_published')
    search_fields = ('title', 'content')
