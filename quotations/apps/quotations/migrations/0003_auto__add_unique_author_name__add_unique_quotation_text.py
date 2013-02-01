# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Author', fields ['name']
        db.create_unique('quotations_author', ['name'])

        # Adding unique constraint on 'Quotation', fields ['text']
        db.create_unique('quotations_quotation', ['text'])


    def backwards(self, orm):
        # Removing unique constraint on 'Quotation', fields ['text']
        db.delete_unique('quotations_quotation', ['text'])

        # Removing unique constraint on 'Author', fields ['name']
        db.delete_unique('quotations_author', ['name'])


    models = {
        'quotations.author': {
            'Meta': {'object_name': 'Author'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'date_of_death': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'quotations.quotation': {
            'Meta': {'object_name': 'Quotation'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quotations'", 'to': "orm['quotations.Author']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '500'})
        }
    }

    complete_apps = ['quotations']