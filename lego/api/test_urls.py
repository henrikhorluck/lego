from django.conf import settings
from django.test import TestCase


class VersionRedirectTestCase(TestCase):

    def test_redirect(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(settings.API_VERSION in response.url)

    def test_404(self):
        response = self.client.get('/api/bad-url/')
        self.assertEqual(response.status_code, 404)