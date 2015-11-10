# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(to='accounts.Author', related_name='posts'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(to='blog.Category', related_name='posts'),
        ),
    ]
