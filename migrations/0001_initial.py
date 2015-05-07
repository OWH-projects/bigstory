# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('titleslug', models.CharField(max_length=100, editable=False)),
                ('link', models.CharField(max_length=300)),
                ('summary', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to=b'foodprowlphotos/', verbose_name=b'Image')),
                ('categorylabel', models.ManyToManyField(to='bestlist.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
