from django.contrib import admin
from django.utils.html import format_html

from taggit.models import Tag

from .models import Post, Category
from .forms import PostForm


def make_published(modeladmin, request, queryset):
    queryset.update(status=Post.PUBLISHED)


make_published.short_description = "Опубликовать выбранные статьи"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'tag_list', 'created', 'status', 'url')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created', 'publish')
    actions = [make_published]
    form = PostForm

    class Media:
        js = (
            'js/froala_settings.js',
        )

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    def url(self, obj):
        return format_html("<a href='{url}'>Перейти</a>".format(url=obj.get_absolute_url()))


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'tag_list', 'parent')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())