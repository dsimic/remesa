# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20141027_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.ForeignKey(related_name='featured_products', to='catalogue.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_in_cop',
            field=models.DecimalField(max_digits=6, decimal_places=3),
            preserve_default=True,
        ),
    ]
