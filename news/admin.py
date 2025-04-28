from django.contrib import admin
from .models import Post, Category
from django.utils.safestring import mark_safe

# Register your models here.
admin.site.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'created_at', 'display_image')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}
    
    # Rasmni kichik ko'rinishda ko'rsatish uchun maxsus funksiya
    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return "Rasm yo'q"
    display_image.short_description = 'Rasm'
    
admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug':('name',)}
