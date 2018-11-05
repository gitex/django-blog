#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path, include, re_path
from django.views.generic import RedirectView

from .views import (
    PostDetailView,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostsByTagView,
    TagListView,
)

app_name = 'blog'

urlpatterns = [
    path('', RedirectView.as_view(url='blog/'), name='index'),
    path('blog/', include([
        path('', PostListView.as_view(), name='post_list'),
        path('create/', PostCreateView.as_view(), name='post_create'),
        path('<slug:slug>/', include([
            path('', PostDetailView.as_view(), name="post_detail"),
            path('update/', PostUpdateView.as_view(), name='post_update'),
            path('delete/', PostDeleteView.as_view(), name='post_delete'),
        ])),


    ])),

    path('tags/', include([
        path('', TagListView.as_view(), name='tags'),
        path('<slug:tag>/', PostsByTagView.as_view(), name='tag'),
    ])),

]