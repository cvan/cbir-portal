import json

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import get_model
from django.http import (HttpResponse, HttpResponseRedirect,
                         HttpResponseBadRequest)
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.http import require_POST

from . import forms, utils
from .models import Image


def home(request):
    """Images home page."""
    images = Image.objects.all()
    images = utils.paginate(request, images, 30)

    image = None
    upload_form = forms.ImageUploadForm(request.POST or None,
                                        request.FILES or None)
    if request.method == 'POST' and upload_form.is_valid():
        if request.FILES:
            image = utils.create_image(request.FILES)

    return render_to_response('images/index.html',
        dict(images=images, upload_form=upload_form, image=image),
        context_instance=RequestContext(request))
