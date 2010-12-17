import os

from django.conf import settings
from django.core import paginator
from django.core.files import File
from django.http import HttpResponseRedirect

from PIL import Image as PILImage

from . import forms
from .models import Image


def get_image_url(image):
    return settings.GALLERY_URL + image


def get_image_path(image):
    return os.path.join(settings.GALLERY_PATH, image)


def get_upload_url(image):
    return settings.IMAGE_UPLOAD_URL + image


def get_upload_path(image):
    return os.path.join(settings.IMAGE_UPLOAD_PATH_FULL, image)


def get_image_size(image):
    return PILImage.open(get_image_path(image)).size


def get_image_info(image):
    src = get_image_url(image)
    w, h = get_image_size(image)
    return dict(src=src, base_src=image, width=w, height=h)


def create_image(files):
    """Given an uploaded file, create an Image object."""
    up_file = files.values()[0]
    try:
        image = Image.objects.get(filename=up_file.name)
    except Image.DoesNotExist:
        image = Image(filename=up_file.name)
    image.file.save(up_file.name, File(up_file), save=True)
    '''
    from PIL import ImageFile
    fp = open(os.path.join(settings.IMAGE_UPLOAD_PATH_FULL, up_file.name), 'rb')
    p = ImageFile.Parser()
    while 1:
        s = fp.read(1024)
        if not s:
            break
        p.feed(s)
    im = p.close()
    jpg_fn = os.path.basename(up_file).replace('.pgm', '.jpg')
    im.save(os.path.join(settings.IMAGE_UPLOAD_PATH_FULL, jpg_fn))
    '''
    return {'name': up_file.name, 'url': image.file.url}


def pgm_upload_handler(request):
    image = None
    form = forms.ImageUploadForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid() and request.FILES:
        image = create_image(request.FILES)
    return (form, image)


def paginate(request, queryset, per_page=20):
    """Get a Paginator, abstracting some common paging actions."""
    p = paginator.Paginator(queryset, per_page)

    # Get the page from the request, make sure it's an int.
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    # Get a page of results, or the first page if there's a problem.
    try:
        paginated = p.page(page)
    except (paginator.EmptyPage, paginator.InvalidPage):
        paginated = p.page(1)

    base = request.build_absolute_uri(request.path)
    paginated.url = u'%s?%s' % (base, request.GET.urlencode())
    return paginated
