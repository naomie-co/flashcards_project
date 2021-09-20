from django.test import TestCase
from django.urls import reverse

"""Tests views and the database models"""

class IndexPageTestCase(TestCase):
    """test that index page returns a status code 200"""
    def test_index_page(self):
        """index_page status code test"""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)