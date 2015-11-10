# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('genres', models.IntegerField(choices=[(1, 'Not Relevant'), (2, 'Male'), (3, 'Female')])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
