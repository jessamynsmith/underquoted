from django.contrib import admin

from underquoted.apps.quotations import models


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']


class QuotationAdmin(admin.ModelAdmin):
    search_fields = ['text', 'author__name']


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Quotation, QuotationAdmin)
