# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minutes', '0004_auto_20151017_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='minutes',
            field=models.ManyToManyField(to='minutes.MtgMinutes'),
        ),
    ]
