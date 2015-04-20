# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgfulltext.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0002_auto_20150419_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quotation',
            name='search_index',
            field=djorm_pgfulltext.fields.VectorField(),
            preserve_default=True,
        ),
    ]
