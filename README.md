CBIR Portal Installation
========================

To download:

    git clone git://github.com/cvan/cibr-portal.git cbir-portal

We're using `pip` to fetch and install our dependencies. If you don't already have it, install it now:

    easy_install pip

Now for installing the dependencies:

    pip install -r requirements/common.txt
    pip install -r requirements/dev.txt

To set up the database schema:

    ./manage.py syncdb

To populate the database table with the images:

    ./manage.py imgdb

To run the Django web server:

    ./manage.py runserver

The paths and global constants can be modified in `settings.py`.
