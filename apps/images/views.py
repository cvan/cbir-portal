import os

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import get_model
from django.http import (HttpResponse, HttpResponseRedirect,
                         HttpResponseBadRequest)
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.http import require_POST

from PIL import Image as img

from . import forms, tasks, utils
from .models import Image


def home(request):
    """Images home page."""
    images = Image.objects.all()
    images = utils.paginate(request, images, 40)

    upload_form = forms.ImageUploadForm(request.POST or None,
                                        request.FILES or None)
    if request.method == 'POST' and upload_form.is_valid():
        if request.FILES:
            image = utils.create_image(request.FILES)

    images = []
    for image in os.listdir(settings.GALLERY_PATH)[:40]:
        src = settings.GALLERY_URL + image
        width, height = img.open(os.path.join(settings.GALLERY_PATH, image)).size
        images.append(dict(src=src, width=width, height=height))

    return render_to_response('images/index.html',
        dict(images=images, upload_form=upload_form, image=image or None),
        context_instance=RequestContext(request))
