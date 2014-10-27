# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=150)),
                ('publisher', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CatalogueCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=150)),
                ('description', models.TextField(blank=True)),
                ('catalogue', models.ForeignKey(related_name='categories', to='catalogue.Catalogue')),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='catalogue.CatalogueCategory', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=150)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to=b'product_photo', blank=True)),
                ('manufacturer', models.CharField(max_length=300, blank=True)),
                ('price_in_dollars', models.DecimalField(max_digits=6, decimal_places=2)),
                ('category', models.ForeignKey(related_name='products', to='catalogue.CatalogueCategory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
