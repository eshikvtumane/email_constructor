# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0005_auto_20150212_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='groups',
            field=models.ManyToManyField(to='constructor.CompanyGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='email',
            name='locations',
            field=models.ManyToManyField(to='constructor.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='email',
            name='users',
            field=models.ManyToManyField(to='constructor.Company'),
            preserve_default=True,
        ),
    ]
