# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('html', models.IntegerField(default=0)),
                ('css', models.IntegerField(default=0)),
                ('javascript', models.IntegerField(default=0)),
                ('python', models.IntegerField(default=0)),
                ('django', models.IntegerField(default=0)),
                ('ios', models.IntegerField(default=0)),
                ('android', models.IntegerField(default=0)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
