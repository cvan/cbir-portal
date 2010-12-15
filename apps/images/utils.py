from django.core import paginator
from django.core.files import File

from .models import Image


def create_image(files):
    """Given an uploaded file, create an Image object."""
    up_file = files.values()[0]
    image = Image()
    image.file.save(up_file.name, File(up_file), save=True)
    return {'name': up_file.name, 'url': image.file.url}


def paginate(request, queryset, per_page=20):
    """
    Get a Paginator, abstracting some common paging actions.
    """
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
