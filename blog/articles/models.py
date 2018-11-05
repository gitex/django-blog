from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from taggit.managers import TaggableManager
from froala_editor.fields import FroalaField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.PUBLISHED)


class Post(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    title = models.CharField(_('название'), max_length=250)
    slug = models.SlugField(_('ссылка'), max_length=250, unique_for_date='publish')
    author = models.ForeignKey(get_user_model(), related_name='blog_posts', on_delete=models.CASCADE)
    body = FroalaField(_('текст'))

    publish = models.DateTimeField(_('опубликовано'), default=timezone.now)
    created = models.DateTimeField(_('создано'), auto_now_add=True)
    updated = models.DateTimeField(_('обновлено'), auto_now=True)
    status = models.CharField(_('статус'), max_length=10, choices=STATUS_CHOICES, default='draft')

    # Managers
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        verbose_name = 'articles'
        verbose_name_plural = 'posts'
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
