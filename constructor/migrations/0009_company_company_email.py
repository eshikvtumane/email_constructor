# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0008_auto_20150212_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_email',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
