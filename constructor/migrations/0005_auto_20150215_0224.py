# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0004_template_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.TextField()),
            ],
            options={
                'db_table': 'Companies',
                'verbose_name': '\u0424\u0438\u0440\u043c\u0430',
                'verbose_name_plural': '\u0424\u0438\u0440\u043c\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Locations',
                'verbose_name': '\u041c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u041c\u0435\u0441\u0442\u043e\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.ForeignKey(to='constructor.Location'),
            preserve_default=True,
        ),
    ]
