from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_public', 'created_at')
    search_fields = ('title', 'content')

# Register your models here.