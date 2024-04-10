# from django.contrib import admin
# from .models import Post

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'created_at')
#     search_fields = ('title', 'content')

from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-created_at',)
    fields = ('title', 'slug', 'content')
    readonly_fields = ('created_at',)