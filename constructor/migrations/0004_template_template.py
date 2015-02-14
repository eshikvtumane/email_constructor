# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0003_auto_20150214_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='template',
            field=models.FileField(default=1, upload_to=b'html_templates'),
            preserve_default=False,
        ),
    ]
