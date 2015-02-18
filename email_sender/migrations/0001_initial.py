# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0011_auto_20150218_0238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField()),
                ('email', models.ForeignKey(to='constructor.Email')),
            ],
            options={
                'db_table': 'Shedules',
                'verbose_name': '\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043e\u0442\u043f\u0440\u0430\u0432\u043a\u0438',
                'verbose_name_plural': '\u0420\u0430\u0441\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043e\u0442\u043f\u0440\u0430\u0432\u043e\u043a',
            },
            bases=(models.Model,),
        ),
    ]
