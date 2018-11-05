from collections import Counter

from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db.models import Count, F
from django.db.models.functions import Lower, Upper
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)

from taggit.models import Tag, TaggedItem

from .models import Post
from .forms import PostForm


class PostDetailView(DetailView):
    model = Post
    template_name = 'articles/detail.html'
    context_object_name = 'post'


class PostListView(ListView):
    model = Post
    template_name = 'articles/list.html'
    context_object_name = 'posts'
    paginate_by = settings.PAGINATE_BY


class PostSetAuthorMixin(object):
    model = Post

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        if kwargs['instance'] is None:
            kwargs['instance'] = Post()

        kwargs['instance'].author = self.request.user

        return kwargs


class PostCreateView(PostSetAuthorMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'articles/create.html'


class PostUpdateView(PostSetAuthorMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'articles/create.html'


class PostDeleteView(DeleteView):
    model = Post


class PostsByTagView(ListView):
    model = Post
    template_name = 'articles/list.html'
    context_object_name = 'posts'
    paginate_by = settings.PAGINATE_BY
    queryset = Post.objects.all()

    def get_queryset(self):
        tag_name = self.kwargs.get('tag')

        if tag_name:
            tag = get_object_or_404(Tag, slug=tag_name)
            return self.queryset.filter(tags__in=[tag])
        return self.queryset


class TagListView(ListView):
    template_name = 'tags/list.html'
    context_object_name = 'tags'
    paginate_by = 100
    queryset = TaggedItem.objects\
        .values(name=Upper('tag_id__name'), slug=F('tag_id__slug'))\
        .annotate(count=Count('tag_id__name'))\
        .order_by('-count')