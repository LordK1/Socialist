# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151031_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pulished_date',
            new_name='published_date',
        ),
    ]
