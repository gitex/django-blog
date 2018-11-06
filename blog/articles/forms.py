#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from froala_editor.widgets import FroalaEditor
from django_select2.forms import Select2Widget, Select2TagWidget, ModelSelect2TagWidget
from taggit.models import Tag

from .models import Post, Category


class CustomModelSelect2TagWidget(ModelSelect2TagWidget):
    queryset = Tag.objects.all()
    search_fields = ['name__icontains']
    model = Tag

    def value_from_datadict(self, data, files, name):
        values = super().value_from_datadict(data, files, name)

        valid_values = list(filter(lambda x: x.isdigit(), values))
        invalid_values = list(filter(lambda x: not x.isdigit(), values))

        for value in invalid_values:
            instance_pk = self.model.objects.create(name=value).pk
            valid_values.append(instance_pk)

        return valid_values


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label=_('body'),
        widget=FroalaEditor(
            plugins=settings.FROALA_EDITOR_PLUGINS,
        )
    )

    category = forms.ModelChoiceField(
        label=_('category'),
        queryset=Category.objects.all(),
        widget=Select2Widget
    )

    tags = forms.ModelMultipleChoiceField(
        label=_('tags'),
        queryset=Tag.objects.all(),
        widget=CustomModelSelect2TagWidget,
        required=False,

    )

    class Meta:
        model = Post
        fields = ['title', 'slug', 'category', 'body', 'tags', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.initial['tags'] = [tag for tag in self.instance.tags.all()]

    def clean(self):
        if self.has_error('tags'):
            print(self.cleaned_data.get('tags'))

        return super().clean()