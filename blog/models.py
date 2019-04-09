from typing import Tuple

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    """Post Model"""
    DRAFT: str = 'DRAFT'
    PUBLISHED: str = 'PUBLISHED'
    STATUS_CHOICES = (
        (DRAFT, _('Draft')),
        (PUBLISHED, _('Published'))
    )
    title = models.CharField(_('Title'), max_length=50)
    subtitle = models.CharField(_('SubTitle'), max_length=50, default='')
    body = models.TextField(_('Body'))
    status = models.CharField(_('Status'),
                              choices=STATUS_CHOICES,
                              max_length=9,
                              default=DRAFT)
    slug = models.CharField(_('Slug'), max_length=255, blank=True)
    published = models.DateTimeField(_('Published Timestamp'), blank=True)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    modified = models.DateTimeField(_('Created'), auto_now=True)

    @classmethod
    def get_duplicated(cls, slug: str, instance) -> Tuple:
        """
        Return a duplicated if exist
        :param slug: an Slug
        :return: Tuple and Object
        """
        try:
            return True, cls.objects.exclude(pk=instance.pk).get(slug=slug)
        except cls.DoesNotExist:
            return False, None

    def __str__(self):
        return self.title

    @classmethod
    def set_slug(cls, instance):
        """return a slug"""
        slug: str = slugify(instance.title)
        exists, duplicated = cls.get_duplicated(slug, instance)
        if exists:
            try:
                new_last_char = int(duplicated[-1]) + 1
            except ValueError:
                new_last_char = 1
            return f'{slug}-{new_last_char}'
        return slug

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = Post.set_slug(self)
        super(Post, self).save()
