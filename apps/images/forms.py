from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _, ugettext_lazy as _lazy

from images.models import Image


MSG_IMAGE_REQUIRED = _lazy(u'You have not selected an image to upload.')
MSG_IMAGE_LONG = _lazy(
    'Please keep the length of your image filename to %(max)s '
    'characters or fewer. It is currently %(length)s characters.')


class ImageUploadForm(forms.Form):
    """Image upload form."""
    file = forms.ImageField(error_messages={'required': MSG_IMAGE_REQUIRED,
                                            'max_length': MSG_IMAGE_LONG},
                             max_length=settings.MAX_FILENAME_LENGTH)
    class Meta:
        model = Image
        fields = ('file')

    def clean_file(self):
        file = self.cleaned_data['file']
        if file.content_type not in settings.IMAGE_ALLOWED_MIMETYPES:
            msg = _(u'The image must be of the following types: %s.' %
                    ', '.join(settings.IMAGE_ALLOWED_EXTENSIONS))
            raise forms.ValidationError(msg)
        return file
