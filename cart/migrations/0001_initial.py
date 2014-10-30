# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField(default=1, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)])),
                ('deliver_every', models.CharField(default=b'1M', max_length=150, choices=[(b'1T', b'One time order'), (b'1W', b'1 week'), (b'2W', b'2 weeks'), (b'3W', b'3 weeks'), (b'1M', b'1 month'), (b'2M', b'2 months'), (b'3M', b'3 months'), (b'4M', b'4 months'), (b'5M', b'5 months'), (b'6M', b'6 months')])),
                ('cart', models.ForeignKey(related_name='cart_items', to='cart.Cart')),
                ('product', models.ForeignKey(to='catalogue.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
