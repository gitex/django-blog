from django.contrib import admin
from django.utils.html import format_html

from taggit.models import Tag

from .models import Post
from .forms import PostForm


def make_published(modeladmin, request, queryset):
    queryset.update(status=Post.PUBLISHED)


make_published.short_description = "Опубликовать выбранные статьи"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'tag_list', 'created', 'status', 'url')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created', 'publish')
    actions = [make_published]
    form = PostForm

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    def url(self, obj):
        return format_html("<a href='{url}'>Перейти</a>".format(url=obj.get_absolute_url()))
