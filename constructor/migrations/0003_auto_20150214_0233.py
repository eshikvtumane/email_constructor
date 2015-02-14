# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0002_emailtoimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='image',
            field=models.ImageField(default=1, upload_to=b'email_images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='template',
            name='html',
            field=models.FileField(upload_to=b'html_templates'),
        ),
    ]
