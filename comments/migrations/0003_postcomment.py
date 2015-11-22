# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0002_update_user_email_field_length'),
        ('comments', '0002_auto_20151122_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('comment_ptr', models.OneToOneField(primary_key=True, serialize=False, to='django_comments.Comment', auto_created=True, parent_link=True)),
                ('content', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
            bases=('django_comments.comment',),
        ),
    ]
