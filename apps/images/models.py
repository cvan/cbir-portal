from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import simplejson
from django.utils.translation import ugettext_lazy as _

import datetime

'''
class Image(models.Model):
    image = models.CharField(_('filename'), max_length=255, default='',
                             null=True)
    active = models.BooleanField(_('active'), default=1)
    created = models.DateTimeField(_('date created'), null=True,
                                   default=datetime.datetime.now)

    similar_images = models.ManyToManyField('self', symmetrical=False,
                                            through='ImageRelationship',
                                            related_name='images')
    # Upon upload of a new image, clear all these.

    class Meta:
        db_table = 'images'

    def __unicode__(self):
        return self.filename

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
        get_latest_by = 'date_added'


class ImageRelationship(models.Model):
    image = models.ForeignKey(Image, related_name='images_similarities')
    similar_image = models.ForeignKey(Image, related_name='similar_to')

    class Meta:
        db_table = 'images_similarities'
'''


class Image(models.Model):
    """An image attached to an object using a generic foreign key."""
    file = models.ImageField(upload_to=settings.IMAGE_UPLOAD_PATH,
                             max_length=settings.MAX_FILEPATH_LENGTH)
    created = models.DateTimeField(null=True, default=datetime.datetime.now)
    similar_images = models.ManyToManyField('self', symmetrical=False,
                                            through='ImageRelationship',
                                            related_name='images')
    # Upon upload of a new image, clear all these.

    class Meta:
        db_table = 'images'
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __unicode__(self):
        return self.file.name

    def get_absolute_url(self):
        return self.file.url


class ImageRelationship(models.Model):
    image = models.ForeignKey(Image, related_name='images_similarities')
    similar_image = models.ForeignKey(Image, related_name='similar_to')

    class Meta:
        db_table = 'images_similarities'
