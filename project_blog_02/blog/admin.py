from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Category, Location, Post


admin.site.site_header = 'Администрирование Блога'
admin.site.site_title = 'Блог'


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'category',
        'location',
        'is_published',
    )
    list_editable = (
        'is_published',
        'category',
    )
    search_fields = ('title', 'text')
    list_filter = ('is_published', 'category', 'location')
    list_display_links = ('title',)
    date_hierarchy = 'pub_date'
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'is_published',
        'created_at',
    )
    list_editable = ('is_published',)
    search_fields = ('title', 'description')
    list_filter = ('is_published',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    empty_value_display = '-пусто-'


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
        'created_at',
    )
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('is_published',)
    list_display_links = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)


try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass
