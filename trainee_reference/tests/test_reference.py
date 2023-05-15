from pprint import pprint

from django.test import TestCase
from edc_reference.site import site_reference_configs


class TestReference(TestCase):

    def test_(self):
        pprint(site_reference_configs.registry)