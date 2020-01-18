from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin)
    list_display = ('title', 'is_public', 'created_at')

# Register your models here.