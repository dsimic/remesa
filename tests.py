from django.test import TestCase
from django.test.client import RequestFactory, Client


class RemesaTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.c = Client()

    def testDown(self):
        pass

    def test_send_activation_email(self):
        response = self.c.post(
            '/accounts/register/',
            {'username': 'susan12',
             'email': 'susan@example.com',
             'password1': '0000',
             'password2': '0000'
             })
        self.assertEqual(response.status_code, 302)
