# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quotation'
        db.create_table('quotations_quotation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='quotations', to=orm['quotations.Author'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('quotations', ['Quotation'])

        # Adding model 'Author'
        db.create_table('quotations_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('date_of_death', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('quotations', ['Author'])


    def backwards(self, orm):
        # Deleting model 'Quotation'
        db.delete_table('quotations_quotation')

        # Deleting model 'Author'
        db.delete_table('quotations_author')


    models = {
        'quotations.author': {
            'Meta': {'object_name': 'Author'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'date_of_death': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'quotations.quotation': {
            'Meta': {'object_name': 'Quotation'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quotations'", 'to': "orm['quotations.Author']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['quotations']