# Generated by Django 5.0.6 on 2024-06-28 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_review_time_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='time_created',
        ),
    ]