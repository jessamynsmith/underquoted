from django import test
from django.contrib import admin

from quotations import models
from quotations import admin as quotations_admin


class AdminTest(test.TestCase):

    def test_admin(self):
        apps = admin.site._registry

        self.assertEqual(quotations_admin.AuthorAdmin, type(apps[models.Author]))
        self.assertEqual(quotations_admin.QuotationAdmin, type(apps[models.Quotation]))
