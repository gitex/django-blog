#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

from froala_editor.widgets import FroalaEditor
from django_select2.forms import Select2MultipleWidget, Select2Widget, Select2TagWidget, HeavySelect2MultipleWidget
from taggit.models import Tag

from .models import Post, Category


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=FroalaEditor)

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=Select2Widget
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=Select2MultipleWidget,
        required=False,
    )

    class Meta:
        model = Post
        fields = ['title', 'slug', 'category', 'body', 'tags', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initial['tags'] = [tag for tag in self.instance.tags.all()]
