from django.contrib import admin
from .models import Post, Category

# Register your models here.
admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}
    
admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name',)}
