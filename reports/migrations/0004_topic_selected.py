# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_topic_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]
