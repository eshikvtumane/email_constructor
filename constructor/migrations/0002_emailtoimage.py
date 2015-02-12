# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('constructor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailToImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.ForeignKey(to='constructor.Email')),
                ('image', models.ForeignKey(to='constructor.Image')),
            ],
            options={
                'db_table': 'EmailToImage',
                'verbose_name': '\u041f\u0438\u0441\u044c\u043c\u043e \u043a \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044e',
                'verbose_name_plural': '\u041f\u0438\u0441\u044c\u043c\u0430 \u043a \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f\u043c',
            },
            bases=(models.Model,),
        ),
    ]
