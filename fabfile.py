#!/usr/bin/env python
"""Fabfile using only commands from buedafab (https://github.com/bueda/ops) to
deploy this app to remote servers.
"""

import os
from fabric.api import *

from buedafab.test import test, django_test_runner as _django_test_runner, lint
from buedafab.deploy.types import django_deploy as deploy
from buedafab.environments import (django_development as development,
                                   django_production as production,
                                   django_localhost as localhost,
                                   django_staging as staging)
from buedafab.tasks import (setup, restart_webserver, rollback, enable,
                            disable, maintenancemode, rechef)

# For a description of these attributes, see https://github.com/bueda/ops

env.unit = "MSU-CSE484-Content-Based-Image-Retrieval"
env.path = "/home/ec2-user/%(unit)s" % env
env.scm = "git://github.com/zachriggle/%(unit)s.git" % env
env.scm_http_url = "http://github.com/zachriggle/%(unit)s" % env
env.root_dir = os.path.abspath(os.path.dirname(__file__))
env.test_runner = _django_test_runner

env.pip_requirements = ["requirements/common.txt"]
env.pip_requirements_dev = ["requirements/dev.txt"]
env.pip_requirements_production = ["requirements/production.txt"]
