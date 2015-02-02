from django import test
from django.http import HttpRequest
from tastypie.http import HttpUnauthorized

from quotations.libs.auth import MethodAuthentication


class MethodAuthenticationTest(test.TestCase):

    def setUp(self):
        self.auth = MethodAuthentication()
        self.request = HttpRequest()

    def test_is_authenticated_get(self):
        self.request.method = 'GET'

        is_authed = self.auth.is_authenticated(self.request)

        self.assertEqual(True, is_authed)

    def test_is_authenticated_post(self):
        self.request.method = 'POST'

        is_authed = self.auth.is_authenticated(self.request)

        self.assertEqual(HttpUnauthorized, type(is_authed))
