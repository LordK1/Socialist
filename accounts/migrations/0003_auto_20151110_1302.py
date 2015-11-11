# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20151031_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='genres',
            field=models.IntegerField(default=1, choices=[(1, 'Not Relevant'), (2, 'Male'), (3, 'Female')]),
        ),
    ]
