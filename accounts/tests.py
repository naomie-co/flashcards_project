from django.test import TestCase
from django.urls import reverse
"""Tests account views"""


class LogPagesTestCase(TestCase):

    def test_log_in_page(self):
        """test that login page returns a status code 200"""
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)

    def test_sign_up_page(self):
        """test that sing_up page returns a status code 200"""
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)
    
    def test_log_out_page(self):
        """Test that logout page returns a status code 302"""
        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)
    