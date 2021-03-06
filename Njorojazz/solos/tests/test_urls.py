from django.test import TestCase 
from django.core.urlresolvers import resolve

from solos.views import index 

class SolosUrlsTestCase(TestCase):
    def test_root_url_uses_index_view(self):
        """
        Test that the roor url resolves to the correct view
        """
        root = resolve('/')
        self.assertEqual(root.func, index)

