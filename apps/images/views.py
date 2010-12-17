import os
import re

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import get_model
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.utils.html import strip_tags
from django.views.decorators.http import require_POST

from . import forms, tasks, utils
from .models import Image, Photo

from tools import lemur, query


def home(request):
    """Images home page."""
    upload_form, upload_img = utils.pgm_upload_handler(request)
    if request.method == 'POST' and upload_form.is_valid() and request.FILES:
        return HttpResponseRedirect(reverse('images.pgm-results',
                                            args=[upload_img['name']]))

    images = Photo.objects.all()
    images = utils.paginate(request, images)
    return render_to_response('images/index.html',
                              dict(images=images, upload_form=upload_form),
                              context_instance=RequestContext(request))


def similar(request, filename):
    """Similar images page."""
    try:
        image_words = file(os.path.join(settings.CBIR_PATH, 'docs',
                                        filename)).read()
    except IOError:
        raise Http404

    upload_form, upload_img = utils.pgm_upload_handler(request)
    if request.method == 'POST' and upload_form.is_valid() and request.FILES:
        return HttpResponseRedirect(reverse('images.pgm-results',
                                            args=[upload_img['name']]))

    image_dict = utils.get_image_info(filename)

    words = strip_tags(image_words).split('\n')[3].strip().split()
    words = '<DOC 1>\n%s\n</DOC>\n' % '\n'.join(words)
    results = lemur.executeQuery(words)

    images = [utils.get_image_info(result) for result in results]

    return render_to_response('images/similar.html',
                              dict(image=image_dict, images=images,
                                   upload_form=upload_form),
                              context_instance=RequestContext(request))


def pgm_results(request, filename):
    """PGM query results page."""
    image = get_object_or_404(Image, filename=filename)

    upload_form, upload_img = utils.pgm_upload_handler(request)
    if request.method == 'POST' and upload_form.is_valid() and request.FILES:
        return HttpResponseRedirect(reverse('images.pgm-results',
                                            args=[upload_img['name']]))

    results = query.execute_query(image.get_absolute_path())
    image_dict = dict(base_src=image.filename, src=image.get_absolute_url())

    images = [utils.get_image_info(result) for result in results]

    return render_to_response('images/results.html',
                              dict(image=image_dict, images=images,
                                   upload_form=upload_form),
                              context_instance=RequestContext(request))
