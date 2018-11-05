#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from froala_editor.widgets import FroalaEditor

from .models import Post


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=FroalaEditor)

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags', 'status']

