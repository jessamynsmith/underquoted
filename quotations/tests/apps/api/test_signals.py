from django import test
from django.contrib.auth import models as auth_models
from tastypie.models import ApiKey


class SignalsTest(test.TestCase):

    def test_signals(self):
        user = auth_models.User(username='jody')
        user.save()

        api_keys = ApiKey.objects.filter(user=user)

        self.assertEqual(1, len(api_keys))
