#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

from regcore import tests as coretests
from regulations import tests as regulationstests

imported_tests = [coretests, regulationstests]

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.test_settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = DiscoverRunner()
    failures = test_runner.run_tests(["tests",], extra_tests=imported_tests)
    sys.exit(bool(failures))