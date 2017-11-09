# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0003_auto_20150419_1201'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ('name',)},
        ),
    ]
