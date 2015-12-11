# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_topic_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
