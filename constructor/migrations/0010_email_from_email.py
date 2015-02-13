# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0009_company_company_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='from_email',
            field=models.CharField(default='ex@example.com', max_length=255),
            preserve_default=False,
        ),
    ]
