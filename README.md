CBIR Portal Installation
========================

To download:

    git clone git://github.com/cvan/cbir-portal.git

We're using `pip` to fetch and install our dependencies. If you don't already have it, install it now:

    easy_install pip

Now for installing the dependencies:

    pip install -r requirements/common.txt -r requirements/dev.txt

To set up the database schema:

    ./manage.py syncdb

To populate the images database:

    ./manage.py imgdb

To run the Django web server:

    ./manage.py runserver

Global variables are defined in `settings.py`.

The paths to the CBIR package are defined in `environment.py` and `settings.py`.
