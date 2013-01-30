from django.contrib import admin

from quotations.apps.quotations import models

admin.site.register(models.Author)
admin.site.register(models.Quotation)
