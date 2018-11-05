from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from taggit.managers import TaggableManager
from froala_editor.fields import FroalaField


class TimeStampedModel(models.Model):
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    title = models.CharField(_('title'), max_length=250)
    slug = models.SlugField(_('slug'), max_length=250, unique=True)
    description = models.TextField(_('description'))
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    tags = TaggableManager(blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.title


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.PUBLISHED)


class Post(TimeStampedModel):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    title = models.CharField(_('title'), max_length=250)
    slug = models.SlugField(_('slug'), max_length=250, unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    body = FroalaField(_('body'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    publish = models.DateTimeField(_('publish'), default=timezone.now)
    status = models.CharField(_('status'), max_length=10, choices=STATUS_CHOICES, default='draft')

    # Managers
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
