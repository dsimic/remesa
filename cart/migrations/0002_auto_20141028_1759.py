# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20141027_1936'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('cart', models.ForeignKey(related_name='cart_items', to='cart.Cart')),
                ('product', models.ForeignKey(to='catalogue.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='cartelement',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartelement',
            name='product',
        ),
        migrations.DeleteModel(
            name='CartElement',
        ),
    ]
