import datetime
import os

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import simplejson
from django.utils.translation import ugettext_lazy as _


class Photo(models.Model):
    filename = models.CharField(default='', blank=True, max_length=255)
    src = models.CharField(default='', blank=True, max_length=255)
    width = models.CharField(default='', blank=True, max_length=255)
    height = models.CharField(default='', blank=True, max_length=255)


class Image(models.Model):
    """An image attached to an object using a generic foreign key."""
    file = models.ImageField(upload_to=settings.IMAGE_UPLOAD_PATH,
                             max_length=settings.MAX_FILEPATH_LENGTH)
    filename = models.CharField(default='', blank=True, max_length=255)
    created = models.DateTimeField(null=True, default=datetime.datetime.now)
    similar_images = models.ManyToManyField('self', symmetrical=False,
                                            through='ImageRelationship',
                                            related_name='images')

    class Meta:
        db_table = 'images'
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        get_latest_by = 'created'

    def __unicode__(self):
        return self.file.name

    def get_absolute_url(self):
        return self.file.url

    def get_absolute_path(self):
        return os.path.join(settings.MEDIA_ROOT, self.file.name)


class ImageRelationship(models.Model):
    image = models.ForeignKey(Image, related_name='images_similarities')
    similar_image = models.ForeignKey(Image, related_name='similar_to')

    class Meta:
        db_table = 'images_similarities'
