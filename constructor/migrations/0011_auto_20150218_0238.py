# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0010_email_from_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='email',
            name='locations',
        ),
        migrations.AlterField(
            model_name='email',
            name='users',
            field=models.ManyToManyField(to='constructor.Company', null=True, blank=True),
            preserve_default=True,
        ),
    ]
