import os

from django.conf import settings
from django.core.management.base import BaseCommand

from images.models import Photo
from images import utils


class Command(BaseCommand):
    help = "Build the database of images in `%s`." % settings.GALLERY_PATH

    def handle(self, *args, **options):
        if Photo.objects.all().count() == settings.GALLERY_SIZE:
            self.stdout.write('Image database already built\n')
            return
        for image in os.listdir(settings.GALLERY_PATH):
            try:
                image = Photo.objects.get(filename=image)
            except Photo.DoesNotExist:
                src = settings.GALLERY_URL + image
                w, h = utils.get_image_size(image)
                Photo(filename=image, src=src, width=w, height=h).save()
            self.stdout.write('Imported "%s"\n' % image)
