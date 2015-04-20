# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgfulltext.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(null=True, db_index=True, serialize=False, editable=False, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quotation',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(null=True, db_index=True, serialize=False, editable=False, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quotation',
            name='author',
            field=models.ForeignKey(related_name='underquoted', to='quotations.Author'),
            preserve_default=True,
        ),
    ]
