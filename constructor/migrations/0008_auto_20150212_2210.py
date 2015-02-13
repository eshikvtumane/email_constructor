# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0007_email_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='multimedia_link',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
