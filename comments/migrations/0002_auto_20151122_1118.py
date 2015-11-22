# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0002_update_user_email_field_length'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcomment',
            name='comment_ptr',
        ),
        migrations.DeleteModel(
            name='PostComment',
        ),
    ]
