# Generated by Django 5.0.6 on 2024-06-28 17:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_remove_review_time_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=False,
        ),
    ]
