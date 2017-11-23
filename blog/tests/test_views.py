from django.test import TestCase
from django.contrib.auth import get_user_model


class UrlTests(TestCase):

    def test_homepage(self):
        res = self.client.get('/blog/')
        self.assertEqual(res.status_code, 200)

    def test_homepage_redirect(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 302)


class HomePageTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='some_user')


