# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0005_auto_20150215_0224'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'CompanyGroups',
                'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='company',
            name='group',
            field=models.ForeignKey(default=1, to='constructor.CompanyGroup'),
            preserve_default=False,
        ),
    ]
