# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('multimedia_link', models.URLField()),
            ],
            options={
                'db_table': 'Emails',
                'verbose_name': '\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u043e\u0435 \u043f\u0438\u0441\u044c\u043c\u043e',
                'verbose_name_plural': '\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u044b\u0435 \u043f\u0438\u0441\u044c\u043c\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'email_images')),
            ],
            options={
                'db_table': 'Images',
                'verbose_name': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('html', models.TextField()),
            ],
            options={
                'db_table': 'Templates',
                'verbose_name': '\u0428\u0430\u0431\u043b\u043e\u043d \u043f\u0438\u0441\u044c\u043c\u0430',
                'verbose_name_plural': '\u0428\u0430\u0431\u043b\u043e\u043d\u044b \u043f\u0438\u0441\u0435\u043c',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='email',
            name='email_template',
            field=models.ForeignKey(to='constructor.Template'),
            preserve_default=True,
        ),
    ]
