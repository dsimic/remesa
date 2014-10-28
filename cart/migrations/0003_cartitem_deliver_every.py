# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20141028_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='deliver_every',
            field=models.CharField(default=b'1M', max_length=150, choices=[(b'W', b'1 week'), (b'2W', b'2 weeks'), (b'3W', b'3 weeks'), (b'1M', b'1 month'), (b'2M', b'2 months'), (b'3M', b'3 months'), (b'4M', b'4 months'), (b'5M', b'5 months'), (b'6M', b'6 months')]),
            preserve_default=True,
        ),
    ]
